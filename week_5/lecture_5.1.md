
## Homework Review

Double check if your output (when running your `flight_finder.py`) matches what the instruction told you it should match:

```
Origin           │ Destination      │ Route
─────────────────┼──────────────────┼──────────────────────────────
Albuquerque      │ San Diego        │ Albuquerque > Chicago > San Diego
Boston           │ Chicago          │ Boston > Chicago
Albuquerque      │ Paris            │ -
San Diego        │ Chicago          │ -
```

### Formatted Strings

To format strings in Python you should use `f-strings`:
```python
name = "Sam Adams"
age = 19

print(f"{name:<10} | {age:>2}")
print(f"{'George':<10} | {5:>2}")
```

The code above will produce the following output:
```
Sam Adams  | 19
George     |  5
```

We can also center content and automatically round numbers to a certain decimal:
```python
f"{3.1415:^10.2f}"
# '   3.14   '
```

The general syntax is:
- put a `f` before a string `""`
- use `{` and `}` inside a string to indicate the position of a placeholder
- use values or variables before the `:`
- follow with a `<`, `>`, `^` and a number `n` to left, right-, or center-align the value into `n` spaces
- (optional) for decimals: use `.xf` after your alignment instructions to indicate the result should be a float rounded to `x` decimals.
- If you ever wanted to use `{` or `}` normally inside a formatted string you can do so by escaping them:

```python
f"Hello \{World\}"
# Hello {World}
```
