from business.Commands.Command import Command
from infra.error.exceptionUser import ExceptionUser
from infra.error.exceptionPassword import ExceptionPassword

class AddUserCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        username = input("Digite o username: ")
        password = input("Digite a password: ")
        try:
            self.controller.add(username, password)
        except ExceptionUser as e:
            print(f"Erro ao cadastrar usuário: {e}")
        except ExceptionPassword as e:
            print(f"Erro ao cadastrar usuário: {e}")