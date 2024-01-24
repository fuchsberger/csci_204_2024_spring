"""
This example demonstrates importing from a subfolder as well as from a python build-in module.
"""

import math
import helpers.math as math2


a = math.sqrt(9)
b = math2.power(3, 1)

print(a, b)
