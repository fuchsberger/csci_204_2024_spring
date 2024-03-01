import math
from clist import CList, CNode

class Processor(CList):
  def __init__(self):
    """Creates a new processor.
    DO NOT MODIFY"""
    super().__init__()
    self.time_passed = 0

def boot(self, stop_after = math.inf):
  """Starts up the tick loop.
  If time_passed reaches 5000 ms kills system process # 1.

  If time_passed reaches stop_after ms, prints all running processes and stops further ticks terminating the server.

  DO NOT MODIFY
  """
  while self.time_passed < stop_after:
    self.tick()

    if self.time_passed == 5000:
      self.kill(1)

  print(self)

def spawn(self, ms = math.inf, repeat=False): # 1 point
  """
  Creates and adds a new process with the given running time to the CPU.
  Should also print the following line:
  <time>: Spawned #<id>
  """
  pass

def tick(self): # 3 points
  """
  Deducts 5 ms from the current process (no effect on infinite processes).
    - If the remaining time of the process reached 0, despawns the process.
      - If the despawned node was set to repeat, immediatly respawns a node with the same id, time and respawn attributes.

  Then moves on to the next process.

  Should also print the following lines (if applicable):
  <time>: Terminated # <id>
  <time>: Spawned # <id>
  """
  pass

def kill(self, id): # 1 point
  """
  Finds and terminates a specific process with the given ID (despawn it).
  Should also print the following line:
  <time>: Killed # <id>
  """
  pass

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

class Process(CNode):
  def __init__(self, id, time, repeat):
    """Creates a new process.
    DO NOT MODIFY
    """
    super().__init__(id)
    self.repeat = repeat
    self.time_total = time
    self.time_remaining = time
