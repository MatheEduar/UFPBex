from relatorio import Relatorio
class RelatorioAcessoPDF(Relatorio):
    def cabecalho(self):
        print("Relatório de Acesso (PDF)")
        print("-----------------------")

    def gerar_estatisticas(self, dados_acesso):
        print("Estatísticas de Acesso:")
        for usuario, acessos in dados_acesso.items():
            print(f"- {usuario}: {acessos} acessos")

    def rodape(self):
        print("-----------------------")
        print("Fim do Relatório")