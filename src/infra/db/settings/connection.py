from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "postgresql+psycopg2",
            "postgres",
            "negan",
            "localhost",
            "5432",
            "clean_database"
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):                   # Cria a base de dados com a engine
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)   # Cria uma sessão do banco de dados
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
