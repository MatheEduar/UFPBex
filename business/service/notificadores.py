class PrintObserver:
    def atualizar(self, mensagem):
        print(f"[PrintObserver] {mensagem}")

class LoggerObserver:
    def atualizar(self, mensagem):
        with open("log.txt", "a") as log:
            log.write(f"[Logger] {mensagem}\n")
