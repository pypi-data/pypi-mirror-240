# igogo 🐎🏎️

Execute several jupyter cells at the same time

> Have you ever just sited and watched a long-running jupyter cell?
> **Now, you can continue to work in the same notebook freely**

https://user-images.githubusercontent.com/25539425/227176976-2bdda463-ecc9-4431-afec-6d31fbd4c214.mov

---

## Use Cases
1) **You have a long-running cell, and you need to check something.
   You can just start the second cell without interrupting a long-running cell**.
   > **Example:** you run a machine learning train loop and want to immediately save the model's weights or check metrics.
   > With `igogo` you can do so without interrupting the training.
2) **If you need to compare the score of some function with different parameters, you can run several
   functions at the same time and monitor results**. 
   > **Example:** you have several sets of hyperparameters and want to compare them.
   > You can start training two models, monitoring two loss graphs at the same time. 
3) **Process data in chunks**. Check processed data for validity
   > **Example:** you do data processing in steps. With `igogo` you can execute several steps at the same time
   > and process data from the first processing step in the second processing step in chunks.
   > Also, you can quickly check that the first step produces the correct results

## Install

Igogo is available through PyPi:

```bash
pip install igogo
```

## Wait, isn't it just a background job? No.

- **No multithreading, no data races, no locks**.
You can freely operate with your notebook variables without the risk of corrupting them.
- **Beautiful output**. When several cells execute in parallel,
all printed data is displayed in the corresponding cell's output. No more twisted and messed out concurrent outputs.
- **Easily cancel jobs, wait for completion, and start the new ones**.
- **Control execution of jobs through widgets**.

## Usage

At the core of igogo is collaborative execution. Jobs need to explicitly allow other jobs to execute through `igogo.yielder()`. Mind that regular cells also represent a job.

Placing `igogo.yielder()` in code that is not executed in igogo job is not a mistake. It will return immediately. So, you don't need to care about keeping `igogo.yielder()` only in igogo jobs. You can place it anywhere

To start an igogo job, you can use `%%igogo` cell magic or function decorator. 

```python
import igogo

@igogo.job
def hello_world(name):
    for i in range(3):
        print("Hello, world from", name)
        
        # allows other jobs to run while asleep
        # also can be `igogo.yielder()`
        igogo.sleep(1)  
    return name
```

Call function as usual to start a job:

```python
hello_world('igogo'), hello_world('other igogo');
```

https://user-images.githubusercontent.com/25539425/227186815-6870e348-46e6-4086-a89b-be416c0cc1a7.mov

### Configure Jobs

Decorator `@igogo.job` has several useful parameters. 

- `kind`\
   Allows to set how to render output. Possible options: `text`, `markdown`, `html` Default: `text`
- `displays`\
   As igogo job modify already executed cell, it needs to have spare placeholders for rich output.
   This parameter specifies how many spare displays to spawn. Default: `1`
- `name`\
   User-friendly name of igogo job.
- `warn_rewrite`\
   Should warn rewriting older displays? Default: `True`
- `auto_display_figures`\
   Should display pyplot figures created inside igogo automatically? Default: `True`

Markdown example:

https://user-images.githubusercontent.com/25539425/227203729-af94582c-8fe2-40fe-a6f0-6489a374a88f.mov

### Display Additional Data

Pyplot figures will be automatically displayed in igogo cell.

You can also use `igogo.display` inside a job to display any other content or several figures. Mind that displays must be pre-allocated by specifying displays number in `igogo.job(displays=...)`

```python
import numpy as np
import matplotlib.pyplot as plt
import igogo

def experiment(name, f, i):
     x = np.linspace(0, i / 10, 100)
     fig = plt.figure()
     plt.plot(
         x,
         f(x)
     )
     plt.gca().set_title(name)
     igogo.display(fig)
     
     fig = plt.figure()
     plt.scatter(
         x,
         f(x)
     )
     plt.gca().set_title(name)
     igogo.display(fig)
     igogo.sleep(0.05)
```

As noted in "Configure jobs" section, `igogo` jobs have limited number of displays.
If you try to display more objects than job has, warning will be shown and the oldest displays will be overwritten.

### Cell Magic

The same way with `%%igogo`:

```python
%load_ext igogo
```

```python
%%igogo
name = 'igogo'
for i in range(3):
     print("Hello, world from", name)
     igogo.sleep(1)
```

### Widgets

All executed `igogo` jobs spawn a widget that allows to kill them. Jobs are not affected by `KeyboardInterrupt`

### Killing Jobs

Apart from killing through widgets, `igogo` jobs can be killed programmatically.

- `igogo.stop()` \
   Can be called inside `igogo` job to kill itself.
- `igogo.stop_all()`\
   Stops all running `igogo` jobs
- `igogo.stop_latest()`\
   Stops the latest `igogo` job. Can be executed several times.
- `igogo.stop_by_cell_id(cell_id)`\
   Kills all jobs that were launched in cell with `cell_id` (aka [5], cell_id=5).

Also, you can stop jobs of one specific function.

- `hello_world.stop_all()`\
   Stops all `igogo` jobs created by `hello_world()`

## Supported Clients

Currently, `igogo` runs fully correct on:

- Jupyter Lab
- Jupyter

Runs but has problems with output from igogo jobs. Jobs are executed, but there could be problems with widgets and output:
- VSCode. For some reason it does not update display data. Therefore, no output is produced.
- DataSpell. It displays `[object Object]` and not output.
- Colab. It does not support updating content of executed cells

## More Examples

[**Check out pretty notebooks**](https://github.com/alexdremov/igogo/tree/main/examples)

---

### Train model and check metrics 

https://user-images.githubusercontent.com/25539425/227651626-cba8a317-a986-4971-9639-84cdb388e2d3.mov

Also, you can modify training parameters, freeze/unfreeze layers, switch datasets, etc. All you need is to place `igogo.yielder()` in train loop.

### Process data and montitor execution

```python
import igogo
import numpy as np
from tqdm.auto import tqdm
%load_ext igogo

raw_data = np.random.randn(100000, 100)
result = []
```

```python
def row_processor(row):
    return np.mean(row)
```

```python
%%igogo
for i in tqdm(range(len(raw_data))):
    result.append(row_processor(raw_data[i]))
    igogo.yielder()
```

```python
result[-1]
```

### Process data in chunks

```python
import igogo
import numpy as np
from tqdm.auto import tqdm
%load_ext igogo

raw_data = np.random.randn(5000000, 100)

igogo_yield_freq = 32
igogo_first_step_cache = []

result = []
```

```python
%%igogo

for i in tqdm(range(len(raw_data))):
    processed = np.log(raw_data[i] * raw_data[i])
    igogo_first_step_cache.append(processed)
    
    if i > 0 and i % igogo_yield_freq == 0:
        igogo.yielder()  # allow other jobs to execute
```

```python
%%igogo

for i in tqdm(range(len(raw_data))):
    while i >= len(igogo_first_step_cache):  # wait for producer to process data
        igogo.yielder()
    
    result.append(np.mean(igogo_first_step_cache[i]))
    
```

https://user-images.githubusercontent.com/25539425/227224077-a3ce664c-cb52-4aa2-a3fe-71ac5a03cdeb.mov


