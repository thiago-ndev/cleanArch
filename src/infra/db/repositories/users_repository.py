from src.infra.db.entities.users import UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                database.session.add(new_registry)
                database.session.commit()

            except Exception as ex:
                database.session.rollback()
                raise ex
