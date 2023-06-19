"""
This module provides a decorator that adds exception handling to functions.
"""
import logging
# pylint: disable=C0103
def logged(exception, mode):
    """ 
    Parameterized decorator that adds exception handling to functions
    and logs them based on the specified mode.

    Parameters:
    exception (Exception): Class or tuple of classes of exceptions to be caught.
    mode (str): Logging mode: "console" or "file".

    Returns:
    wrapper (function): Wraps the input function and adds exception handling.
    """
    def decorator(func):
        """
        Inner decorator that wraps the input function.

        Parameters:
        func (function): The input function to be wrapped.

        Returns:
        wrapper (function): Wraps the input function and adds
        exception handling.
        """ # pylint: disable= R1710
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(level=logging.INFO, filename=
                                        "exception.log",filemode="a")
                    logging.error(e)
        return wrapper
    return decorator
