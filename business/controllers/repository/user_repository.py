from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_username(self, username):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def update_user(self, user):
        pass

    @abstractmethod
    def delete_user(self, username):
        pass