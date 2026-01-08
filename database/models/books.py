from database.models import BaseModel
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey


class User(BaseModel):
    __tablename__ = 'bools'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int] # 1$ = 100 cents
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))


