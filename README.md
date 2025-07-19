# Pyvalidly

**Pyvalidly** is a lightweight, zero-dependency Python library for validating dictionaries with simple rules, custom functions, and optional coercion.

Inspired by Pydantic's power but built for simplicity, speed, and flexibility — especially useful when you want to avoid creating full-blown classes.

---

## Features

- Simple schema-based dictionary validation  
- Optional type coercion (e.g. str → int)  
- Custom validators (e.g. `is_email`, `is_positive`)  
- Optional and nullable fields  
- No external dependencies

---

## Installation

```
pip install pyvalidly
```


## Usage
### Basic Validation 
```
from pyvalidly import validate

schema = {
    "name": str,
    "age": int
}

data = {
    "name": "Alice",
    "age": 25
}

validate(data, schema)  # Returns True if valid
```

### With optional and nullable fields

```
schema = {
    "name": str,
    "nickname": {"type": str, "optional": True},
    "bio": {"type": str, "nullable": True}
}
```

### Custom validators

```
from pyvalidly import is_email

schema = {
    "email": is_email
}
```

### Type Coercion

```
schema = {
    "age": int
}

data = {"age": "30"}  # str input

validate(data, schema, coercion=True)  # Will coerce "30" → 30
```

## Project Structure
```
pyvalidly/
├── core.py
├── exceptions.py
├── validators.py
├── __init__.py
└── tests/
    └── test_core.py
```

## License

MIT License

## Contribute

Pull requests, suggestions, and stars are welcome!
If this helped you, consider supporting the project.


## Contact

Made with love by Deepak singh — https://github.com/dark00infinity