import os
import inspect


def doc(arg):
    """Docstring decorator.

    arg:    Docstring text or object.
    """
    def decorator(func):
        if type(arg) is str:
            func.__doc__ = arg
        elif inspect.isclass(arg):
            func.__doc__ = arg.__doc__
        else:
            func.__doc__ = None

        return func
    return decorator
