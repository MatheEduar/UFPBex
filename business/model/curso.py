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

    def to_dict(self):
        return {
            "nome": self.nome,
            "codigo": self.codigo,
            "area": self.area,
            "periodos": self.periodos,
            "cargaHorariatotal": self.cargaHorariatotal,
            "cargaHorariaOptativa": self.cargaHorariaOptativa,
            "cargaHorariaMinima": self.cargaHorariaMinima,
            "cargaHorariaMaxima": self.cargaHorariaMaxima,
            "qtdFavoritos": self.qtdFavoritos
        }

    def adicionar_observador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

        print(len(self._observadores))    

    def notificar_observadores(self, mensagem):
        for o in self._observadores:
            o.atualizar(mensagem)
