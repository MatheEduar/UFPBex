from business.Commands.Command import Command

class ShowCursoCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        codigo = input("Digite o código do curso que deseja buscar: ")
        curso = self.controller.listCurso(codigo)
        if curso:
            print(f"Nome: {curso.nome}, Código: {curso.codigo}, Área: {curso.area}, Períodos: {curso.periodos}, Carga Horária Total: {curso.cargaHorariatotal}, Carga Horária Optativa: {curso.cargaHorariaOptativa}, Carga Horária Mínima: {curso.cargaHorariaMinima}, Carga Horária Máxima: {curso.cargaHorariaMaxima}, Quantidade de Favoritos: {curso.qtdFavoritos}")
        else:
            print("Curso não encontrado.")
