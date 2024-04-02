#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises the NameError exception with an optional message.

    Args:
        message (str): The optional message to be included in the exception.

    Raises:
        NameError: It's always raised with the message provided.
    """
    raise NameError(message)
