from infra.dao.user_dao import UserDAO
from business.model.user import User
import json

class UserDAOImpl(UserDAO):
    def __init__(self, file_path="data/users.json"):
        self.file_path = file_path
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data_dict = json.load(file)
                users = [User(username, password) for username, password in data_dict.items()]
                return users
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def _save_users(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data_dict = {user.username: user.password for user in self.users}
            json.dump(data_dict, file, indent=4)

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_all_users(self):
        return self.users

    def create_user(self, user):
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