### The complication of mutpy
- This bite requires `mutpy` to pass too which adds complication
- `mutpy` will mutate the code in `color.py` and expect those tests to fail
- In order to get this to work, I needed to set the `return_value` dependant on the call parms
- To achieve this, I needed to use `patch` as a *context manager* and use a `side_effect` function to set the `return_value`
