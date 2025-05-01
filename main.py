from view.curso_form import CursoForm
from view.user_form import UserForm

def main():
    formUser = UserForm()
    formCurso = CursoForm()

    choices = {
        1: formUser.menu,
        2: formCurso.menu
    }

    while True:
        print("\nEscolha uma opção:")
        print("1 - Menu de Usuário")
        print("2 - Menu de Curso")
        print("0 - Sair")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 0:
            print("Encerrando o programa.")
            break

        acao = choices.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
