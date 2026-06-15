from datetime import datetime
from sqlalchemy import DateTime, func, Float, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine



ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/library?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(
        DateTime, insert_default=func.now(), default=func.now(), comment="创建时间")

    update_time: Mapped[datetime] = mapped_column(
        DateTime, insert_default=func.now(), default=func.now(), onupdate=func.now(), comment="修改时间")


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍ID")
    title: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")
    price: Mapped[float] = mapped_column(Float, comment="价格")

""""


class Author(Base):
    pass


class Publisher(Base):
    pass
"""

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)