from business.model.user import User
from service.validations import Validation
from infra.user_dao import UserDAO
from business.controllers.repository.facadeSingleton import FacadeSingleton
from business.report import logAdapter

log = logAdapter.LoggerAdapter(use_print=True)

class ControllerUsers:
    def __init__(self, dao: UserDAO):
        self.facade = FacadeSingleton()
        self.dao = dao 
      
    def add(self, username, password):
        self.facade.add_user(username, password)
        log.info(f"Usuário {username} adicionado com sucesso!")

    def listUser(self, username):
        return self.facade.get_user(username)

    def listAll(self):
        users = self.facade.get_all_users()
        for user in users:
            log.info(user.username)

    def editUser(self, username, userChange):
        self.facade.update_user(username, userChange)
        log.info(f"Usuário {username} alterado para {userChange} com sucesso!")

    def deleteUser(self, username):
        self.facade.delete_user(username)
        log.info(f"Usuário {username} deletado com sucesso!")