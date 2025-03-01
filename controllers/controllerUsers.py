from model.user import User
from service.validations import Validation

class ControllerUsers(User):
    def __init__(self):
        self.users = []

    def add(self, username, password):
        validarUsuario = Validation()
        validarUsuario.validateUserName(username)
        validarUsuario.validatePassword(password)

        user = User(username, password)
        self.users.append(user)
        print(f"Usuário {username} adicionado com sucesso!")

        

    def listUser(self, username):
        for user in self.users:
            if(user.username == username):
                return username
            else: 
                return "Usuário não encontrado!"
        

    def listAll(self):
        for user in self.users:
            print(user.username)

    def editUser(self, username, userChange):
        for user in self.users:
            if(username == user.username):
                user.username = userChange
                print(f"Usuário {username} alterado para {userChange} com sucesso!")
            else:
                print("Usuário não encontrado!")


    def deleteUser(self, username):
        for user in self.users:
            if(username == user.username):
                self.users.remove(user)
                print(f"Usuário {username} deletado com sucesso!")
            else:
                print("Usuário não encontrado!")
        