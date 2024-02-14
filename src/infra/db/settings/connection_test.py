# from sqlalchemy import text         usado para text query SQL
import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensive test")            # Adiciona um marcador para pular esse teste
def test_criar_a_engine_da_base_de_dados():
    db_connection_handle = DBConnectionHandler()
    engine = db_connection_handle.get_engine()
    assert engine is not None
