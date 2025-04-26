from business.controllers.controllerUsers import ControllerUsers
from infra.user_dao_impl import UserDAOImpl
from business.Commands.UserCommands import AddUserCommand, ListAllUsersCommand, DeleteUserCommand, ShowUserCommand, EditUserCommand

class UserForm:
    def __init__(self):
        controller = ControllerUsers(UserDAOImpl())
        self.commands = {
            1: AddUserCommand.AddUserCommand(controller),
            2: ShowUserCommand.ShowUserCommand(controller),
            3: ListAllUsersCommand.ListAllUsersCommand(controller),
            4: EditUserCommand.EditUserCommand(controller),
            5: DeleteUserCommand.DeleteUserCommand(controller)
        }

    def menu(self):
        opcao = 0
        while opcao != 6:
            opcao = int(input('''===== UFPBex =====\n
1) Cadastrar Usuário.
2) Mostrar Usuário.
3) Mostrar todos os Usuários.
4) Editar Usuário.
5) Deletar Usuário.
6) Sair do programa.\n
> '''))

            command = self.commands.get(opcao)
            if command:
                command.execute()
