class DataException(Exception):
    def __init__(self, mensagem="Dados inválidos!"):
        super().__init__(mensagem)