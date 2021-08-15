Pretty happy with my solution. However I could have used `yield` rather than a generator expression. Here is the comparison:

### From the Solution:
```
def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    with open(data) as f:
        for line in f:
            yield int(line.strip().split()[0])

```

### From my version:
```
def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    with open(STATS) as f:
        return (int(line.strip().split()[0]) for line in f.readlines())
```