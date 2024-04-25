def describe_exception(exception):
    """
    Returns a string containing the exception type, message and line_nos.
    """
    return f"{type(exception).__name__}: {exception} at line {exception.__traceback__.tb_lineno}"
