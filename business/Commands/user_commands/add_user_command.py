from business.commands.command import Command

class AddUserCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        username = input("Digite o username: ")
        password = input("Digite a password: ")
        self.controller.add(username, password)