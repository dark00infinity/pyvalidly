import pytest
from pyvalidly import validate, Schema, ValidationError
from pyvalidly.validations import is_email, is_url, min_value, max_value, min_length, max_length

def test_validate_simple_types():
    rules = {
        "name": str,
        "age": int
    }
    data = {"name": "Alice", "age": 30}
    assert validate(data, rules) == data

def test_validate_with_lambda():
    rules = {
        "score": (int, lambda x: x >= 0)
    }
    data = {"score": 10}
    assert validate(data, rules) == data

def test_validate_with_type_and_lambda_fail():
    rules = {
        "age": (int, lambda x: x > 18)
    }
    data = {"age": 15}
    with pytest.raises(ValidationError):
        validate(data, rules)

def test_missing_field_raises():
    rules = {"email": str}
    data = {}
    with pytest.raises(ValidationError):
        validate(data, rules)

def test_email_validation():
    rules = {"email": is_email}
    valid = {"email": "test@example.com"}
    invalid = {"email": "not-an-email"}
    assert validate(valid, rules) == valid
    with pytest.raises(ValidationError):
        validate(invalid, rules)

def test_url_validation():
    rules = {"website": is_url}
    valid = {"website": "https://example.com"}
    invalid = {"website": "badurl"}
    assert validate(valid, rules) == valid
    with pytest.raises(ValidationError):
        validate(invalid, rules)

def test_min_max_value():
    rules = {
        "age": min_value(18),
        "score": max_value(100)
    }
    valid = {"age": 20, "score": 95}
    invalid = {"age": 16, "score": 120}
    assert validate(valid, rules) == valid
    with pytest.raises(ValidationError):
        validate(invalid, rules)

def test_length_constraints():
    rules = {
        "username": min_length(3),
        "password": max_length(8)
    }
    valid = {"username": "abc", "password": "secret"}
    invalid = {"username": "ab", "password": "toolongpassword"}
    assert validate(valid, rules) == valid
    with pytest.raises(ValidationError):
        validate(invalid, rules)

def test_schema_usage():
    user_schema = Schema({
        "name": str,
        "email": is_email,
        "age": (int, lambda x: x >= 18)
    })
    valid = {"name": "Alice", "email": "a@b.com", "age": 20}
    assert user_schema.validate(valid) == valid

def test_coercion_success():
    rules = {"age": int}
    data = {"age": "25"}
    assert validate(data, rules, coerce=True) == {"age": 25}

def test_coercion_failure():
    rules = {"age": int}
    data = {"age": "twenty"}
    with pytest.raises(ValidationError):
        validate(data, rules, coerce=True)