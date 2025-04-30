from infra.dao.user_dao_impl import UserDAOImpl
from business.controllers.repository.userRepository import UserRepository  

class UserRepositoryImpl(UserRepository):
    def __init__(self):  
        self.dao = UserDAOImpl()

    def get_user_by_username(self, username):
        return self.dao.get_user_by_username(username)

    def get_all_users(self):
        return self.dao.get_all_users()

    def create_user(self, user):
        self.dao.create_user(user)

    def update_user(self, user):
        self.dao.update_user(user)

    def delete_user(self, username):
        self.dao.delete_user(username)