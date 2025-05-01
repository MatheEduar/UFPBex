from business.controllers.controller_cursos import ControllerCursos
from business.commands.curso_commands import add_curso_command, delete_curso_command, edit_curso_command, list_all_cursos_command, show_curso_command, undo_command

class CursoForm:
    def __init__(self):
        controller = ControllerCursos()
        self.commands = {
            1: add_curso_command.AddCursoCommand(controller),
            2: delete_curso_command.DeleteCursoCommand(controller),
            3: list_all_cursos_command.ListAllCursosCommand(controller),
            4: edit_curso_command.EditCursoCommand(controller),
            5: show_curso_command.ShowCursoCommand(controller),
            6: undo_command.UndoCursoCommand(controller)
        }

    def menu(self):
        opcao = 0
        while opcao != 7:
            opcao = int(input('''===== UFPBex - Cursos =====\n
1) Cadastrar Curso.
2) Deletar Curso.
3) Listar todos os Cursos.
4) Editar Curso.
5) Buscar Curso.
6) Desfazer última ação                              
7) Sair do menu de cursos.\n
> '''))
            if opcao in self.commands:
                self.commands[opcao].execute()