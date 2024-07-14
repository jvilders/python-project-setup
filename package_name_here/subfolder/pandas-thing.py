"""Experimenting with pandas, which requires stubs to be installed for mypy to shut up."""

import pandas as pd

d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=d)
