from business.controllers.repository.facadeSingleton import FacadeSingleton
from business.report import loggerAdapter

class ControllerUsers:
    def __init__(self):
        self.facade = FacadeSingleton()
        self.log = loggerAdapter.LoggerAdapter(use_print=True)
      
    def add(self, username, password):
        self.facade.add_user(username, password)
        self.log.info(f"Usuário {username} adicionado com sucesso!")

    def listUser(self, username):
        return self.facade.get_user(username)

    def listAll(self):
        users = self.facade.get_all_users()
        for user in users:
            self.log.info(user.username)

    def editUser(self, username, userChange):
        self.facade.update_user(username, userChange)
        self.log.info(f"Usuário {username} alterado para {userChange} com sucesso!")

    def deleteUser(self, username):
        self.facade.delete_user(username)
        self.log.info(f"Usuário {username} deletado com sucesso!")