from .exceptions import ValidationError
from .validations import is_validation_func

def validate(data, rules, coerce=False):
    validated = {}

    for field, rule in rules.items():
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")

        value = data[field]

        try:
            # Handle tuple (type, lambda)
            if isinstance(rule, tuple):
                expected_type, validator = rule

                # Coerce type if needed
                if coerce:
                    try:
                        value = expected_type(value)
                    except Exception:
                        raise ValidationError(f"Field '{field}' coercion to {expected_type.__name__} failed")
                elif not isinstance(value, expected_type):
                    raise ValidationError(f"Field '{field}' must be of type {expected_type.__name__}")

                # Apply validator
                if callable(validator) and not validator(value):
                    raise ValidationError(f"Field '{field}' failed validation")

            elif isinstance(rule, type):
                # Basic type rule
                if coerce:
                    try:
                        value = rule(value)
                    except Exception:
                        raise ValidationError(f"Field '{field}' coercion to {rule.__name__} failed")
                elif not isinstance(value, rule):
                    raise ValidationError(f"Field '{field}' must be of type {rule.__name__}")

            elif callable(rule):
                # Custom validation function (e.g., is_email)
                if not rule(value):
                    raise ValidationError(f"Field '{field}' failed validation")

            else:
                raise ValidationError(f"Unsupported rule for field '{field}'")

        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError(f"Validation error on field '{field}': {str(e)}")

        # Store coerced or original value
        validated[field] = value

    return validated