class Curso:
    def __init__(self):
        self.nome = None
        self.cargaHorariatotal = None
        self.codigo = None
        self.area = None
        self.periodos = None
        self.cargaHorariaOptativa = None
        self.cargaHorariaMinima = None
        self.cargaHorariaMaxima = None
        self.qtdFavoritos = None

        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def notificar_observadores(self, mensagem):
        for o in self._observadores:
            o.atualizar(mensagem)

    def set_nome(self, novo_nome):
        antigo = self.nome
        self.nome = novo_nome
        self.notificar_observadores(f"Nome do curso alterado de '{antigo}' para '{novo_nome}'")