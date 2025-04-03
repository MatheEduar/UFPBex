from business.controllers.controllerCursos import ControllerCursos
from infra.curso_dao_impl import CursoDAOImpl

class CursoForm:
    def __init__(self):
        self.gerenciador = ControllerCursos(CursoDAOImpl())

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

            if opcao == 1:
                self.cadastrar_curso()
            elif opcao == 2:
                self.deletar_curso()
            elif opcao == 3:
                self.listar_todos()
            elif opcao == 4:
                self.editar_curso()
            elif opcao == 5:
                self.mostrar_curso()

    def cadastrar_curso(self):
        nome = input("Digite o nome do curso: ")
        codigo = input("Digite o código do curso: ")
        area = input("Digite a área do curso: ")
        periodos = int(input("Digite o número de períodos: "))
        carga_horaria_total = int(input("Digite a carga horária total: "))
        carga_horaria_optativa = int(input("Digite a carga horária optativa: "))
        carga_horaria_minima = int(input("Digite a carga horária mínima: "))
        carga_horaria_maxima = int(input("Digite a carga horária máxima: "))
        qtd_favorito = int(input("Digite a quantidade de favoritos: "))
        self.gerenciador.add(nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito)

    def mostrar_curso(self):
        codigo = input("Digite o código do curso que deseja buscar: ")
        curso = self.gerenciador.listCurso(codigo)
        if curso:
            print(f"Nome: {curso.nome}, Código: {curso.codigo}, Área: {curso.area}, Períodos: {curso.periodos}, Carga Horária Total: {curso.cargaHorariatotal}, Carga Horária Optativa: {curso.cargaHorariaOptativa}, Carga Horária Mínima: {curso.cargaHorariaMinima}, Carga Horária Máxima: {curso.cargaHorariaMaxima}, Quantidade de Favoritos: {curso.qtdFavoritos}")
        else:
            print("Curso não encontrado.")

    def listar_todos(self):
        self.gerenciador.listAll()

    def editar_curso(self):
        codigo = input("Digite o código do curso que deseja alterar: ")
        curso_change = input("Digite o novo nome do curso: ")
        self.gerenciador.editCurso(codigo, curso_change)

    def deletar_curso(self):
        codigo = input("Digite o código do curso que deseja deletar: ")
        self.gerenciador.deleteCurso(codigo)