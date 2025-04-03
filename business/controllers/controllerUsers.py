from model.user import User
from service.validations import Validation
from infra.user_dao import UserDAO

class ControllerUsers:
    def init(self):
        self.facade = FacadeSingleton()

    def add(self, username, password):
        self.facade.add_user(username, password)
        print(f"Usuário {username} adicionado com sucesso!")

    def listUser(self, username):
        return self.facade.get_user(username)

    def listAll(self):
        users = self.facade.get_all_users()
        for user in users:
            print(user.username)

    def editUser(self, username, userChange):
        self.facade.update_user(username, userChange)
        print(f"Usuário {username} alterado para {userChange} com sucesso!")

    def deleteUser(self, username):
        self.facade.delete_user(username)
        print(f"Usuário {username} deletado com sucesso!")