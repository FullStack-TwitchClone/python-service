from litestar.config.cors import CORSConfig
from litestar.middleware.rate_limit import RateLimitConfig
from litestar.plugins.sqlalchemy import AsyncSessionConfig, SQLAlchemyAsyncConfig

from .settings import settings

session_config = AsyncSessionConfig(expire_on_commit=False)

db_config = SQLAlchemyAsyncConfig(
    connection_string=settings.DATABASE_URL,
    session_config=session_config,
)

cors_config = CORSConfig(
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
)

rate_limit_config = RateLimitConfig(rate_limit=("minute", 50), exclude=["/schema"])
