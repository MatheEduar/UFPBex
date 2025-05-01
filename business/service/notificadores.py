class PrintObserver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrintObserver, cls).__new__(cls)
        return cls._instance

    def atualizar(self, mensagem):
        print(f"[PrintObserver] {mensagem}")

class LoggerObserver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerObserver, cls).__new__(cls)
        return cls._instance

    def atualizar(self, mensagem):
        with open("log.txt", "a") as log:
            log.write(f"[Logger] {mensagem}\n")
