# Lecture 2.2

## Debugging

![Debugging Meme](images/debugging.png)

**Debugging** has a variety of use cases:
- find problems in code that may not necessarily result in an exception
- identify how the computer moved through your code lines or in fancy words: trace the function call stack
- understand complicated code (especially more archaic forms of code such as assembly)
- inspect the values of variables at certain breakpoints without the need to add print statements in your code

#### Breakpoints
During debugging the program can be run line by line allowing to to inspect the current state of variables and the scope.

**VS Code** By clicking left to a line number you can create a `Breakpoint`. This allows you to run the program and pause once this line is reached before resuming.

#### Activity
Try it out! Find the problem by inspecting the code in `debugme.py` rather than trying to read it out of the code.

## Testing

There are several levels of testing. What you have probably used most frequently so far is rudimentary testing:
```python
def square(n):
  return n * n

result = square(4)
print(result) # should be 16
```
The basic idea is to add print statements while coding to ensure we are still on track or investigate why variables don't contain what they are supposed to contain or functions do not return what they are supposed to return.

This works fine and remains a helpful way of testing, even for intermediate and advanced developers.
The problem often is that those tests get in the way of the code and we have to matricously remove them when done. This leads to another problem. What if i make changes to the function in the future? I need to readd tests and reverify everything behaves correctly. Its also easy to miss critical testing as the focus remains on the main program, not the testing while writing the tests.

Thus you end up deleting/rewriting test code in an endless cycle.

_Instead of writing print statements to inspect the state of variables in the future, consider dropping a breakpoint and use debugging. Much faster!_


## Unit Testing

- Systematic, standardized library for testing code from small files to massive projects.
- Alternative to docstring testing or debugging
- heavy utilized in industry for quality control
- Separation of test code from program code
- Testing all parts of your program simultaniously
- Automatic Test discovery

The unittest library provides a series of assert conveniences, such as: `assertTrue`, `assertIn`, `assertIsInstance` and so on. The full list can be found in the [documentation](https://docs.python.org/3/library/unittest.html).

All of these are build upon the python assert keyword:
```python
assert x == 4, "x should be 4"
```
The statement above would raise an `AssertionError` if the value of x is not 4 with the custom message _"x should be 4"_.

Here is the unitclass wrapper shown in action for the custom math module we created earlier:
```python
import unittest
from .math import power

class MathTests(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)

        with self.assertRaises(ValueError):
            power(2, -1)
```

We can run this file (`test_math.py`) and see a nice summary of how many tests out of how many passed.

For this to work your class must inherit from `unittest.TestCase` and your methods inside the test class must start with `test_`.

Alternatively to running the file we recommend you to use automatic test discovery. In your shell type:
```bash
python -m unittest
```

Python will automatically search for test classes and run **all** files with test classes it can find.

For this to work from your root directory you must place empty `__init__.py` files in each folder and subfolder, including the root directory.

The example code given has this file structure set up properly.


#### Activity

**This Activity is recommended to be completed. It will be featured in the quiz.**

1. Copy the files `math.py` and `test_math.py` from the helpers subfolder to your work directory.

2. Add a function `factorial(n)` to your math module. It should produce a correct result given an integer above `0`.

3. Create a custom exception class (InvalidParameterError) that inherits from the TypeError exception class.

4. Raise this error when anything but an integer other than 1 or higher was provided. Otherwise return the correct result.

5. Add a unittest in `test_math.py` for the new factorial function. It should test for a correct result as well as for raising your INvalidParamterError if parameter wasn't an integer or was below 1.





