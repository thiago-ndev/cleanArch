from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base


class UsersEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


    def __repr__(self):
        return f"{self.id}, {self.first_name}, {self.last_name}, {self.age}"
