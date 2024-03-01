"""
Author: Alexander Fuchsberger
Last Revised: 03/01/2024
Class: CSCI 204

DO NOT CHANGE THIS FILE
"""

import math
from processor import Processor, Process

# TESTING PROCESSOR

print("Start up sequence inititated.\n")

cpu = Processor()

# spawn processes
cpu.spawn(Process(1, math.inf))
cpu.spawn(Process(2, math.inf))
cpu.spawn(Process(3, math.inf))
cpu.spawn(Process(4, 1200))
cpu.spawn(Process(5, 100, True))
cpu.spawn(Process(6, 150))
cpu.spawn(Process(7, math.inf))
cpu.spawn(Process(8, 50))

# prints the processor initally
print(cpu)

# run processor
cpu.boot(10000)

print("\nShut down sequence initialized.")
