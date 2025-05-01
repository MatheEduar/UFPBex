from business.commands.command import Command

class EditUserCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        username = input("Digite o nome do usuário que deseja alterar: ")
        userChange = input("Digite o novo nome: ")
        self.controller.editUser(username, userChange)