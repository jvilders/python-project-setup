from pydantic import ValidationError

from package_name_here import make_model


class TestMakeModel:
    def test_happy_flow(self) -> None:
        string = "a"
        model = make_model(s=string)

        assert model.my_field == [string]

    def test_validation(self) -> None:
        int = 5

        try:
            make_model(s=int)  # type: ignore
        except ValidationError:
            return

        raise ValueError("Model instantiation should not have succeeded")
