from business.Commands.Command import Command

class ShowUserCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        username = input("Digite o usuário que deseja mostrar: ")
        user = self.controller.listUser(username)
        if user:
            print(f"Username: {user.username}, Password: {user.password}")
        else:
            print("Usuário não encontrado.")