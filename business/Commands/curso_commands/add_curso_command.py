from business.commands.command import Command

class AddCursoCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        nome = input("Digite o nome do curso: ")
        codigo = input("Digite o código do curso: ")
        area = input("Digite a área do curso: ")
        periodos = int(input("Digite o número de períodos: "))
        carga_horaria_total = int(input("Digite a carga horária total: "))
        carga_horaria_optativa = int(input("Digite a carga horária optativa: "))
        carga_horaria_minima = int(input("Digite a carga horária mínima: "))
        carga_horaria_maxima = int(input("Digite a carga horária máxima: "))
        qtd_favorito = int(input("Digite a quantidade de favoritos: "))
        self.controller.add(nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito)
