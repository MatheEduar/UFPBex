from business.controllers.repository.facade_singleton import FacadeSingleton
from business.report import logger_adapter
from infra.error.exception_user import ExceptionUser
from infra.error.exception_password import ExceptionPassword

class ControllerUsers:
    def __init__(self):
        self.facade = FacadeSingleton()
        self.log = logger_adapter.LoggerAdapter(use_print=True)
      
    def add(self, username, password):
        try:
            self.facade.add_user(username, password)
            self.log.info(f"Usuário {username} adicionado com sucesso!")
        except ExceptionUser as e:
            print(f"Erro ao cadastrar usuário: {e}")
        except ExceptionPassword as e:
            print(f"Erro ao cadastrar usuário: {e}")

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