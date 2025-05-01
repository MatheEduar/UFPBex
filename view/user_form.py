from business.controllers.controller_users import ControllerUsers
from business.commands.user_commands import add_user_command, delete_user_command, edit_user_command, list_all_users_command, show_user_command

class UserForm:
    def __init__(self):
        controller = ControllerUsers()
        self.commands = {
            1: add_user_command.AddUserCommand(controller),
            2: show_user_command.ShowUserCommand(controller),
            3: list_all_users_command.ListAllUsersCommand(controller),
            4: edit_user_command.EditUserCommand(controller),
            5: delete_user_command.DeleteUserCommand(controller)
        }

    def menu(self):
        opcao = 0
        while opcao != 6:
            opcao = int(input('''===== UFPBex =====\n
1) Cadastrar usuário.
2) Mostrar usuário.
3) Mostrar todos os Usuários.
4) Editar usuário.
5) Deletar usuário.
6) Sair do menu de usuário.\n
> '''))

            command = self.commands.get(opcao)
            if command:
                command.execute()
