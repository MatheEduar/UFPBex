from business.commands.Command import Command

class DeleteCursoCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        codigo = input("Digite o código do curso que deseja deletar: ")
        self.controller.deleteCurso(codigo)
