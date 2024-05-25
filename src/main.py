"""My first an only file for this module."""

from pydantic import BaseModel


class MyModel(BaseModel):
    """My dummy class."""

    my_field: list[str]


def make_model(s: str) -> MyModel:
    """Make an instance of MyModel.

    Accepts a string as input and uses that to instantiate MyModel.
    The instance is returned.
    """
    return MyModel(my_field=[s])


print(make_model("some_string"))
