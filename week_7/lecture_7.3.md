# Activity: Simulating a Processor

The goal is to write a program that simulates how a CPU schedules processes using a circular list (singly). While working in class time you are allowed to collaborate. Please finsih individually as homework.

### Learning Objectives
- Learn about how Processes are scheduled by the operating system
- Learn how to use Infinity in Python
- Practice using circular doubly linked lists
- Practice wrapping custom data into a given ADT.
- Practice inheritance

For this excersise assume that on each "tick" `5` milliseconds pass and then the processor switches the active process to the next one in the list. Processes deduct `5` ms from their remaining time and once the time of a process reaches `0` the processor kills it and removes it from the circular list.

The starting code can be copied from `/processor_simulation` subfolder. It contains the following files:
```bash
main.py        (no need to modify or submit)
clist.py       (no need to modify or submit)
processor.py   (work here!)
```

Take a look at the `Processor` and `Process` constructors and parent classes:
```python
class Processor(CList):
  def __init__(self):
    """Creates a new processor."""
    super().__init__()
    self.time_passed = 0
```
```python
class Process(CNode):
  def __init__(self, id, time, repeat):
    """Creates a new process."""
    super().__init__(id)
    self.repeat = repeat
    self.time_total = time
    self.time_remaining = time
```

**Reflection:** What attributes will end up in instances of the given classes?

### ToDo
You will have to complete the following `Processor` methods:
```python
def spawn(self, ms = math.inf, repeat=False): # 1 point
  """
  Creates and adds a new process with the given running time to the CPU.
  Should also print the following line:
  <time>: Spawned #<id>
  """
  pass
```

```python
def tick(self): # 3 points
  """
  Deducts 5 ms from the current process (no effect on infinite processes).
    - If the remaining time of the process reached 0, despawns the process.
      - If the despawned node was set to repeat, immediatly respawns a node with the same time and respawn trait.

  Then moves on to the next process.

  Should also print the following lines (if applicable):
  <time>: Terminated #<id>
  <time>: Spawned #<id>
  """
  pass
```

```python
def kill(self, id): # 1 point
  """
  Finds and terminates a specific process with the given ID (despawn it).
  Should also print the following line:
  <time>: Killed #<id>
  """
  pass
```

```python
def __str__(self): # 1 point
  """
  Prints a list of the current processes that are running on the server. For example:

  Server has been running for <time> ms.
   ID | Remaining Time
  --------------------
    1 | inf
   11 | 85
    3 | inf
  """
  return ""
```

The `boot(self, stop_after)` method has already been completed. It keeps running `tick()` until we reach `stop_after` miliseconds and manually terminate the server. To test your `kill(self)` function, the server further terminates system process # 1 after `5000` miliseconds.
```python
def boot(self, stop_after = math.inf):
  while self.time_passed < stop_after:
    self.tick()

    if self.time_passed == 5000:
      self.kill(1)
```

### Simulation Example

If you check out `main.py` you will find the processor being set up to run a couple of processes:
- `1`, `2`, `3`, `7`, are system processes and will run indefinitely
- `4` will take `1200` ms to complete
- `5` will take `100` ms to complete and is set to respawn everytime it concludes.
- `6` will take `150` ms to complete
- `8` will take `50` ms to complete

### Reflection Questions
1. Could all finite processes (except 5) finish by the time the server terminates?
2. After how many ms does process `6` terminate?

