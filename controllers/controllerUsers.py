from model.user import User

class ControllerUsers(User):
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def listUser(self, username):
        pass

    def listAll(self):
        pass

    def editUser(self):
        pass

    def deleteUser(self):
        pass