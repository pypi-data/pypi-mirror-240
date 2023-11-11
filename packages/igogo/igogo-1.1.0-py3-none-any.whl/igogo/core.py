#  Copyright (c) 2023.
#  Aleksandr Dremov

import asyncio
import functools
import inspect
import sys
from typing import Dict, List, Any
import traceback

import IPython
import matplotlib.pyplot as plt
from IPython import display as ipydisplay
import greenback
import ipywidgets

from .context import IgogoContext, get_context_or_fail, set_context, AdditionalOutputs
from .output import OutputText, OutputStreamsSetter, OutputObject, OutputTextStyled
from .exceptions import IgogoInvalidContext, IgogoAdditionalOutputsExhausted

_igogo_run_loop = asyncio.get_running_loop()
_all_tasks: Dict[int, List[asyncio.Task]] = dict()
_cell_widgets_display_ids: Dict[int, ipydisplay.DisplayHandle] = dict()
_igogo_count = 0


def _get_currently_running_cells_info():
    """
    Returns a string containing the IDs of all currently running IGOGO cells.

    Returns:
        str: A string containing the IDs of all currently running IGOGO cells.
    """
    global _all_tasks
    keys = map(str, _all_tasks.keys())
    keys = '], ['.join(list(keys))
    if len(keys) > 0:
        keys = '[' + keys + ']'
    return keys


def _log_error(*argc, **kwargs):
    """
    Logs an error message to stderr, including information about currently running IGOGO cells.

    Args:
        *argc: Any arguments to be passed to the print function.
        **kwargs: Any keyword arguments to be passed to the print function, with the addition of 'file' if not present.
    """
    if not 'file' in kwargs:
        kwargs['file'] = sys.stderr
    print('[ IGOGO ]', *argc, **kwargs)
    running_s = _get_currently_running_cells_info()
    if len(running_s) == 0:
        running_s = '<none>'
    print(f'[ IGOGO ] Currently running IGOGO cells: {running_s}', file=kwargs['file'])


def _log_warning(*argc, **kwargs):
    """
    Logs a warning message to stderr.

    Args:
        *argc: Any arguments to be passed to the print function.
        **kwargs: Any keyword arguments to be passed to the print function, with the addition of 'file' if not present.
    """
    if not 'file' in kwargs:
        kwargs['file'] = sys.stderr
    print('[ IGOGO ]', *argc, **kwargs)


def stop():
    """
    Stops the currently executing igogo task.
    """
    value = get_context_or_fail()
    value.task.cancel()


def get_running_igogo_cells():
    """
    Get a list of the keys of all currently running cells.

    Returns:
        list: A list of the keys of all currently running cells.
    """
    global _all_tasks
    _update_all_tasks()
    return list(_all_tasks.keys())


def sleep(delay, result=None):
    """
    Suspend the current task for a specified time.

    Args:
        delay (float): The number of seconds to suspend the task for.
        result (object): An optional result to return when the task resumes.

    Raises:
        IgogoInvalidContext: If there is no active context.
    """
    value = get_context_or_fail()
    value.out_stream.deactivate()
    greenback.await_(asyncio.sleep(delay, result))
    value.out_stream.activate()


def display(object: Any, close_if_figure: bool = True):
    """
    Display an object in the output widget of the current cell.
    Fallback to regular display if there's no igogo job

    This will close pyplot figure by default so that it is not displayed twice

    Args:
        object (Any): The object to display.
        close_if_figure (bool): Close object if it is pyplot figure

    Raises:
        IgogoAdditionalOutputsExhausted: If there are no additional output widgets available.
    """
    try:
        value = get_context_or_fail()
    except IgogoInvalidContext:
        ipydisplay.display(object)
        return
    if value.additional_outputs.is_empty():
        raise IgogoAdditionalOutputsExhausted()
    out = value.additional_outputs.get_next()
    out.add_object(object)
    if isinstance(object, plt.Figure) and close_if_figure:
        plt.close(object)


def clear_output(including_text=True):
    """
    Clear the output of the current igogo cell.

    Args:
        including_text (bool): Whether to clear the text output as well. Default is True.
    """
    value = get_context_or_fail()
    if including_text:
        value.out_stream.stdout.clear()
    value.additional_outputs.clear()


def _update_all_tasks():
    """
    Update the dict of all pending igogo jobs.
    """
    global _all_tasks

    def filter_rule(task: asyncio.Task):
        return not task.done()

    for key in _all_tasks:
        _all_tasks[key] = list(filter(filter_rule, _all_tasks[key]))
    _all_tasks = {k: v for k, v in _all_tasks.items() if len(v) > 0}


def get_pending_tasks():
    """
    Get a list of all pending igogo jobs.

    Returns:
        list: A list of all pending igogo jobs.
    """
    return list(filter(lambda x: 'igogo' in x.get_name(), asyncio.all_tasks(loop=_igogo_run_loop)))


def stop_all():
    """
    Cancel all pending igogo jobs.
    """
    for task in get_pending_tasks():
        task.cancel()


def stop_latest():
    """
    Cancel the latest pending igogo job.
    """
    global _all_tasks
    _update_all_tasks()
    keys = list(_all_tasks.keys())
    if len(keys) == 0:
        _log_error("No running tasks")
        return
    latest_key = max(keys)
    task = _all_tasks[latest_key].pop()
    task.cancel()


def stop_by_cell_id(cell_id):
    """
    Cancel all pending igogo jobs in a given cell.

    Args:
        cell_id (int): The ID of the cell to cancel tasks for.
    """
    global _all_tasks
    _update_all_tasks()

    cell_id = int(cell_id)
    if not cell_id in _all_tasks:
        _log_error(f"There's no running tasks in cell [{cell_id}]")
        return
    for task in _all_tasks[cell_id]:
        task.cancel()


def stop_by_task_name(name):
    """
    Cancel a task by its name.

    Args:
        name (str): The name of the task to cancel.
    """
    global _all_tasks
    _update_all_tasks()

    for cell_id in _all_tasks:
        for task in _all_tasks[cell_id]:
            if task.get_name() == name:
                _log_error(f"Cancelling task {name}")
                task.cancel()
                _update_igogo_widget(cell_id)
                return
    _log_error(f"No task {name} was killed")


def _update_igogo_widget(cell_id):
    """
    Update igogo widget in the specified cell

    Args:
        cell_id (int): The ID of the cell to cancel tasks for.
    """
    global _all_tasks, _cell_widgets_display_ids
    _update_all_tasks()
    cell_id = int(cell_id)
    if not cell_id in _all_tasks:
        _cell_widgets_display_ids[cell_id].update({'text/plain': ''}, raw=True)
        return
    if not cell_id in _cell_widgets_display_ids:
        return
    buttons = []
    for task in _all_tasks[cell_id]:
        task_name = task.get_name()
        button = ipywidgets.Button(description=task_name, icon='stop-circle', layout=ipywidgets.Layout(
            width='auto', height='30px'
        ), button_style='warning', tooltip=f'This will kill {task_name} running in cell [{cell_id}]'
                                   )

        def on_button_clicked(b):
            stop_by_task_name(b.description)

        button.on_click(on_button_clicked)
        buttons.append(button)
    result_widget = ipywidgets.VBox([
        ipywidgets.HBox(buttons)
    ], layout=ipywidgets.Layout(width='100%', display='flex', align_items='flex-end'))
    _cell_widgets_display_ids[cell_id].update(result_widget)


def job(original_function=None, kind='stdout', displays=1, name='', warn_rewrite=True, verbose=False,
        auto_display_figures=True):
    """
    This function decorates a given function with functionality to run it as igogo job.
    Call to decorated function returns dictionary where 'task' represents a spawned job.

    :param kind: output render type, possible options: 'text', 'html', 'markdown'
    :param displays: number of spawned spare displays
    :param name: human-readable igogo job name
    :param warn_rewrite: warn if older displays are rewritten
    :param verbose: print debug igogo information
    :param auto_display_figures: display figures created inside igogo automatically
    """
    global _igogo_count

    def _decorate(function):
        assert not inspect.iscoroutinefunction(function), "Function must not be async"

        @functools.wraps(function)
        def wrapped_function(*args, **kwargs):
            global _igogo_count, _all_tasks, _cell_widgets_display_ids
            ip = IPython.get_ipython()
            ex_count = ip.execution_count

            if ex_count not in _cell_widgets_display_ids:
                widget_handle = ipydisplay.display({'text/plain': ''}, display_id=True, raw=True)
                _cell_widgets_display_ids.setdefault(ex_count, widget_handle)

            output_stream = OutputStreamsSetter(stdout=OutputText(kind=kind), stderr=OutputText(kind='stderr'))
            additional_outputs = AdditionalOutputs(
                count=displays,
                no_warn=not warn_rewrite,
                auto_display_figures=auto_display_figures
            )

            async def func_context_setter():
                if verbose:
                    _log_warning('Ensuring has portal')
                await greenback.ensure_portal()
                context = IgogoContext(
                    task,
                    output_stream,
                    additional_outputs
                )
                set_context(context)
                if verbose:
                    _log_warning('About to set outputs')
                output_stream.activate()
                if verbose:
                    _log_warning('Did set outputs, starting function')
                try:
                    result = function(*args, **kwargs)
                except Exception as e:
                    if verbose:
                        _log_warning('Caught an exception')
                    traceback.print_exc()
                    output_stream.deactivate()
                    if verbose:
                        _log_warning('Deactivated output')
                    return
                output_stream.deactivate()
                if verbose:
                    _log_warning('Deactivated output')
                return result

            coro = func_context_setter()

            if not hasattr(wrapped_function, "tasks"):
                wrapped_function.tasks = []

            task = _igogo_run_loop.create_task(coro)
            wrapped_function.tasks.append(task)

            def done_callback(t):
                if verbose:
                    _log_warning(f'In done_callback, task: {t}')
                _update_igogo_widget(ex_count)
                output_stream.deactivate()
                try:
                    exception = task.exception()
                    if exception is not None:
                        raise exception
                except asyncio.CancelledError:
                    pass

            task.add_done_callback(done_callback)
            task.set_name(f'igogo #{_igogo_count}' + (f'-{name}' if name != '' else ''))
            _igogo_count += 1

            _all_tasks.setdefault(ex_count, [])
            _all_tasks[ex_count].append(task)

            _update_igogo_widget(ex_count)

            return dict(
                task=task
            )

        def stop_all():
            if not hasattr(wrapped_function, "tasks"):
                wrapped_function.tasks = []
            for task in wrapped_function.tasks:
                task.cancel()

        from .yielder import Yielder
        wrapped_function.yielder = Yielder
        wrapped_function.stop_all = stop_all
        wrapped_function.stop = stop
        return wrapped_function

    if original_function:
        return _decorate(original_function)
    return _decorate
