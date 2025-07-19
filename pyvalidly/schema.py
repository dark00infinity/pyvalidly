from .core import validate


class Schema:
    """
    Schema wrapper class to define and reuse validation schemas.

    Example:
        user_schema = Schema({
            "name": str,
            "age": (int, lambda x: x > 0),
            "email": str
        })

        user_schema.validate({
            "name": "John",
            "age": 25,
            "email": "john@example.com"
        })
    """

    def __init__(self, rules: dict):
        self.rules = rules

    def validate(self, data: dict, *, coerce: bool = False):
        return validate(data, self.rules, coerce=coerce)