"""
Here is a decorator that raises exception if the declared field is not in
the model
"""


def serializer_control(func: callable) -> callable:
    """
    Decorator that raises exception if the declared field is not in
    the model

    :param func: wrapped function
    :type func: callable
    :returns: func
    """

    async def wrapper(*args, **kwargs) -> None:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, KeyError):
                raise Exception("There is no such field in the model", e)
            else:
                raise e
    return wrapper
