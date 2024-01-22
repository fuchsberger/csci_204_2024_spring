# Lecture 2.1
## File I/O, Exceptions, OOP

## OOP - Object Oriented Design

OOP: Design Goals

![images/design_goals.png](images/design_goals.png)

OOP: Design Principles

![images/design_principles.png](images/design_principles.png)

### Modules
Do we write thousands of lines of code into one file?
(NO!.....At least very rarely)

We use modules to organize programs.

A python module is a python file that can be imported in another python file.
```python
import math                 # alias the math module. to call a function: math.sqrt(5)
from math import sqrt, sum  # import specific functions/classes. to call: sqrt(5)
from math import *          # import everything (not recommended). to call: sqrt(5)
```

A file can be imported from a subfolder. This only works if the subfolder has an empty `__init__.py` inside:
```python
from subfolder.test import hello
hello()
```

You can also import renaming the module in the process. This is useful if you have two modules with the same name which would normally conflict:
```python
import math
import helpers.math as math2

# math.sqrt()
# math2.power(1, 2)
```

_You can see this example in the files._

A major reason why Python is so popular is its large set of available modules allowing you to quickly perform specific tasks without reinventing the wheel. Here are some examples:

![images/modules.png](images/modules.png)

### Exceptions
What about nonsensical values?

We can raise (and create) exceptions ourselves

![images/exceptions.png](images/exceptions.png)

#### Raising Exceptions
We can manually raise exceptions:
```python
def sqrt(x):
  if not isinstance(x, (int, float)):
    raise TypeError('x must be numeric')
  elif x < 0:
    raise ValueError('x cannot be negative')

  # do the real work here...
```

#### try / except
We can take alternative actions in case an exception would be raised:
```python
age = -1 # an initially invalid choice
while age <= 0:
  try:
    age = int(input("Enter your age in years: "))
    if age <= 0:
      print("Your age must be positive.")

  except (ValueError, EOFError):
    print("Invalid response.")
```

_"Its easier to ask for forgiveness than it is to get permission."_

#### Custom Exceptions

We can create and raise our custom exceptions using what we have learned about classes:

```python
class NegativeHeightException(Exception):
	def __init__(self, val):
		self.val = val

	def __str__(self):
		return(f"Height of {self.val} is incoorect")

def convert_height(inc):
	try:
		if inc < 0:
		  raise NegativeHeightException
		cm = inc * 2.54
		return cm

	except NegativeHeightException:
		print('How can a height be negative? *_*')
```

#### Exceptions - How far do we go?
```python
def sum(values):
  if not isinstance(values, collections.Iterable):
    raise TypeError('parameter must be an iterable type')

  total = 0
  for v in values:
    if not isinstance(v, (int, float)):
      raise TypeError('elements must be numeric')
    total += v

  return total
```

vs
```python
def sum(values):
  total = 0
  for v in values:
    total = total + v

  return total
```

Its okay and preferable to rely on python raising exceptions. Manual raising and custom exceptions are preferred when:
- python doesn't raise correctly by default
- fill gaps
- clarify error message more precisely
- egde cases

#### Practice Activity
Create a function that asks for a temperature in Celsius and returns the temperature in Fahrenheit.

If any non-numeric value was provided raise a custom exception of type `InvalidNumberException` with the message: "Not a number".
