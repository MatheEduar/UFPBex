from business.controllers.controllerUsers import ControllerUsers
from infra.user_dao_impl import UserDAOImpl
from error.exceptionUser import ExceptionUser
from error.exceptionPassword import ExceptionPassword

class UserForm:
    def __init__(self):
        self.gerenciador = ControllerUsers(UserDAOImpl())

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

            if opcao == 1:
                self.cadastrar_usuario()
            elif opcao == 2:
                self.mostrar_usuario()
            elif opcao == 3:
                self.listar_todos()
            elif opcao == 4:
                self.editar_usuario()
            elif opcao == 5:
                self.deletar_usuario()

    def cadastrar_usuario(self):
        username = input("Digite o username: ")
        password = input("Digite a password: ")
        try:
            self.gerenciador.add(username, password)
        except ExceptionUser as e:
            print(f"Erro ao cadastrar usuário: {e}")
        except ExceptionPassword as e:
            print(f"Erro ao cadastrar usuário: {e}")

    def mostrar_usuario(self):
        username = input("Digite o usuário que deseja mostrar: ")
        user = self.gerenciador.listUser(username)
        if user:
            print(f"Username: {user.username}, Password: {user.password}")
        else:
            print("Usuário não encontrado.")

    def listar_todos(self):
        self.gerenciador.listAll()

    def editar_usuario(self):
        username = input("Digite o nome do usuário que deseja alterar: ")
        userChange = input("Digite o novo nome: ")
        self.gerenciador.editUser(username, userChange)

    def deletar_usuario(self):
        username = input("Digite o nome do usuário que deseja deletar: ")
        self.gerenciador.deleteUser(username)