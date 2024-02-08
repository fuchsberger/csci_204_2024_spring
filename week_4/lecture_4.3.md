A few "magic" methods:

```python
# enables x[0]
__get_item__(self)

# enables x[0] = 1
__set_item__(self, item)

# enables len(x)
__len__(self)

# enables print(x)
__str__(x)

# enables x + y
__add__(x, other)

```
