from .repositoryFactory import RepositoryFactory
from business.model.user import User

class FacadeSingleton:
    _instance = None

    def __new__(cls): # correção do método
        if cls._instance is None:
            cls._instance = super(FacadeSingleton, cls).__new__(cls)
            cls._instance.repository = RepositoryFactory.create_user_repository()
        return cls._instance

    def add_user(self, username, password):
        user = User(username, password)
        self._instance.repository.create_user(user)

    def get_user(self, username):
        return self._instance.repository.get_user_by_username(username)

    def get_all_users(self):
        return self._instance.repository.get_all_users()

    def update_user(self, username, userChange):
        user = self._instance.repository.get_user_by_username(username)
        if user:
            user.username = userChange
            self._instance.repository.update_user(user)

    def delete_user(self, username):
        self._instance.repository.delete_user(username)