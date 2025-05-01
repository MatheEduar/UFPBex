from business.commands.command import Command

class EditCursoCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        codigo = input("Digite o código do curso que deseja alterar: ")
        curso_change = input("Digite o novo nome do curso: ")
        self.controller.editCurso(codigo, curso_change)

