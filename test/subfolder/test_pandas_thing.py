import pandas as pd

from python_project_standard.subfolder import df


def test_dummy() -> None:
    assert isinstance(df, pd.DataFrame)
