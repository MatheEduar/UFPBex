import model.user as user

def cadastrar_Usuario(lista):
    nome = input("Digite o seu nome: ")
    nick = input("Digite o nome de usuario: ")
    email = input("Digite o email do usuario: ")
    senha = input("Digite a senha do usuario: ")

    novo_usuario = user.Usuario(nome, nick, email, senha)
    lista.append(novo_usuario)

    print("Usuário cadastrado com sucesso!\n")
    
def editar_Usuario(usuario):
    print("O que deseja editar?\n1 - Username\n2 - Email\n3 - Senha")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        usuario.username = input("Digite o novo username: ")
    elif opcao == "2":
        usuario.email = input("Digite o novo email: ")
    elif opcao == "3":
        usuario.senha = input("Digite a nova senha: ")
    else:
        print("Opção inválida!")
    
    print("Usuário atualizado com sucesso!\n")
            
