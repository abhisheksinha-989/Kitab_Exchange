# models/books.py
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from models.user import User   # only seen by type checkers, never executed at runtime

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    price: int
    is_sold: bool = Field(default=False)
    user_id: int = Field(foreign_key="user.id")
    owner: "User | None" = Relationship(back_populates="books")

class BookCreate(SQLModel):
    title: str
    author: str
    price: int
    user_id: int

class BookRead(SQLModel):
    id: int
    title: str
    author: str
    price: int
    is_sold: bool
    user_id: int

class BookUpdate(SQLModel):
    price: int | None
    is_sold: bool | None