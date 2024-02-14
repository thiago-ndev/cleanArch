from .users_repository import UsersRepository


def test_de_cadastros_de_usuarios():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 23

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
