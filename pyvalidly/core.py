from .validations import is_type, coerce_type
from .exceptions import ValidationError


def validate(data: dict, schema: dict, *, coerce: bool = False):
    """
    Validate a dictionary `data` against a `schema`.

    Args:
        data (dict): The data to validate.
        schema (dict): The validation schema. Keys map to:
                       - a type (e.g., str, int)
                       - or a tuple (type, custom_fn)
        coerce (bool): If True, try to convert values to expected types.

    Raises:
        ValidationError: If any validation fails.
    """
    errors = {}

    for key, rule in schema.items():
        value = data.get(key)

        # Determine expected type and optional custom function
        if isinstance(rule, tuple):
            expected_type, custom_fn = rule
        else:
            expected_type = rule
            custom_fn = None

        # Handle missing key
        if key not in data:
            errors[key] = "Missing field"
            continue

        # Coerce value if enabled
        if coerce:
            try:
                value = coerce_type(value, expected_type)
                data[key] = value  # update coerced value in original dict
            except Exception as e:
                errors[key] = str(e)
                continue

        # Type check
        if not is_type(value, expected_type):
            errors[key] = f"Expected {expected_type.__name__}, got {type(value).__name__}"
            continue

        # Custom validation
        if custom_fn and not custom_fn(value):
            errors[key] = "Custom validation failed"

    if errors:
        raise ValidationError("Validation failed", errors)

    return True