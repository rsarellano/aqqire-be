from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

URL_DATABASE = "postgresql+asyncpg://postgres:admin123$@localhost:5432/aqqire"



engine = create_async_engine(URL_DATABASE)

sessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    db = await sessionLocal()
    try:
        yield db
    finally:
        await db.close()


        