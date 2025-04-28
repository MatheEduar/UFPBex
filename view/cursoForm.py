from business.controllers.controllerCursos import ControllerCursos
# from infra.curso_dao_impl import CursoDAOImpl
from business.Commands.CursoCommands import AddCursoCommand, ShowCursoCommand, EditCursoCommand, ListAllCursosCommand, DeleteCursoCommand

class CursoForm:
    def __init__(self):
        controller = ControllerCursos()
        self.commands = {
            1: AddCursoCommand.AddCursoCommand(controller),
            2: DeleteCursoCommand.DeleteCursoCommand(controller),
            3: ListAllCursosCommand.ListAllCursosCommand(controller),
            4: EditCursoCommand.EditCursoCommand(controller),
            5: ShowCursoCommand.ShowCursoCommand(controller),
        }

    def menu(self):
        opcao = 0
        while opcao != 6:
            opcao = int(input('''===== UFPBex - Cursos =====\n
1) Cadastrar Curso.
2) Deletar Curso.
3) Listar todos os Cursos.
4) Editar Curso.
5) Buscar Curso.
6) Sair do menu de cursos.\n
> '''))
            if opcao in self.commands:
                self.commands[opcao].execute()
