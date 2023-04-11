from config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.user}:{settings.password}@"
    f"{settings.host}:{settings.port}/"
    f"{settings.name}"
)

