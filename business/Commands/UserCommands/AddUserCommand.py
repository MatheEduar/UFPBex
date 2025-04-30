from business.commands.Command import Command
from infra.error.exceptionUser import ExceptionUser
from infra.error.exceptionPassword import ExceptionPassword

class AddUserCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        username = input("Digite o username: ")
        password = input("Digite a password: ")
        self.controller.add(username, password)