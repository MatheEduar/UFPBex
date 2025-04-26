from business.Commands.Command import Command

class DeleteUserCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        username = input("Digite o nome do usuário que deseja deletar: ")
        self.controller.deleteUser(username)