import usuario
import validations
from exceptions import InvalidPasswordException, InvalidUsernameException

def cadastrar_Usuario(lista):

    try:

        nome = input("Digite o seu nome: ")
        nick = input("Digite o nome de usuario: ")

        validations.nickValidation(nick)

        email = input("Digite o email do usuario: ")
        senha = input("Digite a senha do usuario: ")

        validations.passwordValidation(senha, nick, email)

        novo_usuario = usuario.Usuario(nome, nick, email, senha)
        lista.append(novo_usuario)

        print("Usuário cadastrado com sucesso!\n")
    
    except InvalidUsernameException as e:
        print(f"Erro no nome de usuário: {e}")
    except InvalidPasswordException as e:
        print(f"Erro na senha: {e}")
    
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
            
