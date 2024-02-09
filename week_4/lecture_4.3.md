### Lab review
A few "magic" methods:

```python
# enables x[0]
__get_item__(self, index)

# enables x[0] = 1
__set_item__(self, item)

# enables len(x)
__len__(self)

# enables print(x)
__str__(x)

# enables x + y
__add__(x, other)

```

# Stack Workshop - Backtracking

Here is an example: HPAir of using stack for backtracking in its scheduling of flights
Given:
- A set of cities that HPAir serves
- Pairs of city names, each pair represents the origin and destination of one flight
- Pair of cities names each of which represents a request to fly from an origin to a destination

**Find whether or not a path exists between two cities requested by a passenger.**

### General Idea
1. Start from the origin city
2. Find a city that is connected to the current city
3. If the next city is the destination, we are done. Report a route has been found
4. Otherwise go from this city and repeat step 2
5. If we visited all cities and no route is found, we declare the failure


Your `main()` method should return a similar output to the console:
```
Origin           │ Destination      │ Route
─────────────────┼──────────────────┼──────────────────────────────
Albuquerque      │ San Diego        │ Albuquerque > Chicago > San Diego
Boston           │ Chicago          │ Boston > Chicago
Albuquerque      │ Paris            │ -
San Diego        │ Chicago          │ -
```

_I have created a couple of helper functions for you, feel free to ignore and use your own approach instead, as long as it uses the stack a a base._

### Globals

Globals allow you to use variables accross functions:

```python
x = 5

def foo():
  x = 4 # this will not change x on global scope (x defined locally)

def bar()
  global x
  x + 1 # this will change x on global scope (to 6)
```
