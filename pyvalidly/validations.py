import re
from urllib.parse import urlparse


def is_type(value, expected_type):
    """Check if value is of the expected type."""
    return isinstance(value, expected_type)


def coerce_type(value, target_type):
    """Attempt to coerce a value to a target type."""
    if target_type == bool:
        if isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in ("true", "1", "yes", "y"):
                return True
            elif lowered in ("false", "0", "no", "n"):
                return False
            else:
                raise ValueError(f"Cannot coerce string '{value}' to bool")
        return bool(value)
    return target_type(value)


# Built-in utility validations
def is_email(value: str) -> bool:
    """Validate if the value is a valid email address."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))


def is_url(value: str) -> bool:
    """Validate if the value is a valid URL."""
    parsed = urlparse(value)
    return all([parsed.scheme, parsed.netloc])


def matches_regex(value: str, pattern: str) -> bool:
    """Check if a string matches the given regex pattern."""
    return bool(re.match(pattern, value))


def min_value(value, min_val):
    """Ensure value is at least min_val."""
    return value >= min_val


def max_value(value, max_val):
    """Ensure value is at most max_val."""
    return value <= max_val


def min_length(value, min_len):
    """Ensure string/list length is at least min_len."""
    return len(value) >= min_len


def max_length(value, max_len):
    """Ensure string/list length is at most max_len."""
    return len(value) <= max_len