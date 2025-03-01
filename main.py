from model.adm import Adm
from model.gerenciador import cadastrar_Usuario, editar_Usuario

def main():
    usuarios_cadastrados = []
    
    while True:
        print("1 - Cadastrar Usuário\n2 - Editar Usuário\n3 - Listar Usuários\n4 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_Usuario(usuarios_cadastrados)
        elif opcao == "2":
            username = input("Digite o username do usuário que deseja editar: ")
            for user in usuarios_cadastrados:
                if user.username == username:
                    editar_Usuario(user)
                    break
            else:
                print("Usuário não encontrado!\n")
        elif opcao == "3":
            Adm.ListarUsuarios(usuarios_cadastrados)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
