from controllers.controllerUsers import ControllerUsers

class UserForm():
    def __init__(self):
        pass


    def menu(self):
        gerenciador = ControllerUsers()
        opcao = 0

        while(opcao != 6):
            opcao = int(input('''===== UFPBex =====\n
1) Cadastrar Usuário.
2) Mostrar Usuário.
3) Mostrar todos os Usuários.
4) Editar Usuário.
5) Deletar Usuário.
6) Sair do programa.\n
> '''))
            if(opcao == 1):
                self.cadastrar_usuario(gerenciador)
            elif(opcao == 2):
                self.mostrar_usuario(gerenciador)
            elif(opcao == 3):
                self.listar_todos(gerenciador)
            elif(opcao == 4):
                self.editar_usuario(gerenciador)
            elif(opcao == 5):
                self.deletar_usuario(gerenciador)

    
    def cadastrar_usuario(self, gerenciador):
        username = input("Digite o username: ")
        password = input("Digite a password: ")
        gerenciador.add(username, password)

    def mostrar_usuario(self, gerenciador):
        username = input("Digite o usuário que deseja mostrar: ")
        print(gerenciador.listUser(username))

    def listar_todos(self, gerenciador):
        gerenciador.listAll()

    def editar_usuario(self, gerenciador):
        username = input("Digite o nome do usuário que deseja alterar: ")
        userChange = input("Digite o novo nome: ")
        gerenciador.editUser(username, userChange)

    def deletar_usuario(self, gerenciador):
        username = input("Digite o nome do usuário que deseja deletar: ")
        gerenciador.deleteUser(username)