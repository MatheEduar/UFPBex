from view.cursoForm import CursoForm
from view.userForm import UserForm


def main():

    formUser = UserForm()
    formUser.menu()
    formCurso = CursoForm()
    formCurso.menu()



if __name__ == "__main__":
    main()