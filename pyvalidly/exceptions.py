class ValidationError(Exception):
    """
    Raised when validation fails.

    Attributes:
        message (str): Error message.
        errors (dict): Dictionary of field-specific errors.
    """
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.message = message
        self.errors = errors or {}

    def __str__(self):
        if self.errors:
            error_details = ', '.join(f"{k}: {v}" for k, v in self.errors.items())
            return f"{self.message} ({error_details})"
        return self.message