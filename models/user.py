from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(unique=True)
    college: str
    books: list["Book"] = Relationship(back_populates="owner")

class UserCreate(SQLModel):
    name: str
    email: str
    college: str

class UserRead(SQLModel):
    id: int
    name: str
    email: str
    college: str

from models.books import Book
User.model_rebuild()