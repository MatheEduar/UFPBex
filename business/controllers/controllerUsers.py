from model.user import User
from service.validations import Validation
from infra.user_dao import UserDAO

class ControllerUsers:
    def __init__(self, dao: UserDAO):  # Injeta a dependência no construtor
        self.dao = dao
        self.validar_usuario = Validation()

    def add(self, username, password):
        self.validarUsuario.validateUserName(username)
        self.validarUsuario.validatePassword(password)

        user = User(username, password)
        self.dao.create_user(user)
        print(f"Usuário {username} adicionado com sucesso!")

    def listUser(self, username):
        return self.dao.get_user_by_username(username)

    def listAll(self):
        users = self.dao.get_all_users()
        for user in users:
            print(user.username)

    def editUser(self, username, userChange):
        user = self.dao.get_user_by_username(username)
        if user:
            user.username = userChange
            self.dao.update_user(user)
            print(f"Usuário {username} alterado para {userChange} com sucesso!")
        else:
            print("Usuário não encontrado!")

    def deleteUser(self, username):
        try:
            self.dao.delete_user(username)
            print(f"Usuário {username} deletado com sucesso!")
        except ValueError:
            print("Usuário não encontrado!")