from infra.dao.user_dao import UserDAO
from business.model.user import User
from business.service.userValidation import UserValidation

class UserDAOImpl(UserDAO):
    def __init__(self, file_path="data/users.txt"):
        self.file_path = file_path
        self.users = self._load_users()
        self.validarUsuario = UserValidation()

    def _load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                data_list = [line.strip().split() for line in file]
                users = [User(username, password) for username, password in data_list]
                return users
        except FileNotFoundError:
            return []  

    def _save_users(self):
        with open(self.file_path, 'w') as file:
            for user in self.users:
                file.write(f"{user.username} {user.password}\n")

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_all_users(self):
        return self.users

    def create_user(self, user):
        self.validarUsuario.validateUserName(user.username)
        self.validarUsuario.validatePassword(user.password)
        self.users.append(user)
        self._save_users()

    def update_user(self, user):
        for i, existing_user in enumerate(self.users):
            if existing_user.username == user.username:
                self.users[i] = user
                self._save_users()
                return
        raise ValueError("Usuario não encontrado")

    def delete_user(self, username):
        for i, user in enumerate(self.users):
            if user.username == username:
                del self.users[i]
                self._save_users()
                return
        raise ValueError("Usuario não encontrado")