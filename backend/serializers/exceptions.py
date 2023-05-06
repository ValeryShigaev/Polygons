def serializer_control(func: callable) -> callable:
    async def wrapper(*args, **kwargs) -> None:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, KeyError):
                raise Exception("There is no such field in the model", e)
            else:
                raise e
    return wrapper
