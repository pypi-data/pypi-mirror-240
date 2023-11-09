import inspect

__all__ = ("get_function_name",)


def get_function_name():
    """Get name of the function when in its body.

    Returns
    -------
    str
        Name of the function.

    Examples
    --------
    >>> import onekit
    >>> def my_test_function():
    ...     return onekit.get_function_name()
    ...
    >>> my_test_function()
    'my_test_function'
    """
    return inspect.stack()[1].function
