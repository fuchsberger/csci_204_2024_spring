# CSCI 204 Queue and Stack ADT Workshop

1. For the given graph of cities represented as Python dictionary, following the algorithm of Depth First Search (stack solution), complete the following tasks.
```python
{
    'A': ('B', 'C'),
    'B': ('A', 'D', 'E', 'F'),
    'C': ('A', 'F'),
    'D': ('B'),
    'E': ('B', 'F'),
    'F': ('B','C', 'E'),
    'G': ()
}
```

- Draw the diagram represented by the above Python dictionary
- Demonstrate the algorithm how to find if there is a path between the city of `A` and `F` by drawing the changes of the stack;
- Demonstrate the algorithm how to find if there is a path between the city of `C` and `E`;
- Demonstrate the algorithm how to find if there is a path between the city of `A` and `G`.

2. Do the same using the Breath First Search (queue solution)
