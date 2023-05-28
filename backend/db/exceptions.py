from typing import Union


def db_control(func: callable) -> Union[callable, bool]:
    async def wrapper(*args, **kwargs) -> Union[None, bool]:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            return False
    return wrapper


def all_methods_conrol(decorator):
    def decorate(cls):
        for attr in cls.__dict__:  # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate
