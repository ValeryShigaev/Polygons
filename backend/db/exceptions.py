"""
Here is a decorator that returns False on error. There is also a decorator for
decorating class methods, except for methods marked as @classmethod
or @staticmethod
"""

from typing import Type, Union


def db_control(func: callable) -> Union[callable, bool]:
    """
    Decorator for database methods returning False on error

    :param func: wrapped function
    :type func: callable
    :rtype: Union[callable, bool]
    """

    async def wrapper(*args, **kwargs) -> Union[None, bool]:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            return False
    return wrapper


def all_methods_control(decorator: callable) -> callable:
    """
    This function wraps all class methods in the selected decorator.
    Excluding class methods and static methods

    :param decorator: decorator to be used
    :rtype: callable
    """
    def decorate(cls: type) -> type:
        """
        The function that is responsible for assigning the decorator

        :param cls: incoming class
        :rtype: type
        """

        for attr in cls.__dict__:
            # if not classmethod
            if not hasattr(getattr(cls, attr), "__self__"):
                if callable(getattr(cls, attr)):
                    # do wrap
                    setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
