from business.report.relatorio import Relatorio
class RelatorioHTML(Relatorio):
    def cabecalho(self):
        print("<html><head><title>Relatório de Acesso</title></head><body>")

    def gerar_estatisticas(self, dados_acesso):
        print("<h1>Estatísticas de Acesso</h1>")
        print("<ul>")
        for usuario, acessos in dados_acesso.items():
            print(f"<li>{usuario}: {acessos} acessos</li>")
        print("</ul>")

    def rodape(self):
        print("</body></html>")