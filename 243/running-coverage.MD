## Running PyTest
My starter for 10 was to run the following command from inside the main `243` directory:

`python -m pytest --cov=ips test_ips.py`

## Running MutPy
The docs say to use something like `mut.py --target calculator --unit-test test_calculator -m` which I found a bit problematical (on my Windows box at least) so I ran it rather explicitly like this:

`python C:\Users\Craig\python_projects\pybites-temp\venv\Scripts\mut.py --runner pytest --target ips --unit-test test_ips -m`

*Note that in the above, I also needed to specify `pytest` as the `runner`*

## Additional
I had to set up a Python 3.7 environment to run this. I needed to install:

- `pytest`
- `pytest-cov`
- `mutpy`
