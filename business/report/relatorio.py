from abc import ABC, abstractmethod

class Relatorio(ABC):
    def gerar_relatorio(self, dados_acesso):
        self.cabecalho()
        self.gerar_estatisticas(dados_acesso)
        self.rodape()

    @abstractmethod
    def cabecalho(self):
        pass

    @abstractmethod
    def gerar_estatisticas(self, dados_acesso):
        pass

    @abstractmethod
    def rodape(self):
        pass