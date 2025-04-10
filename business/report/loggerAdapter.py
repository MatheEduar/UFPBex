import logging

class LoggerAdapter:
    def __init__(self, use_print=True):
        self.use_print = use_print

        # Configuração básica do logging
        logging.basicConfig(
            level=logging.INFO,
            format='[%(levelname)s] %(asctime)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        self.logger = logging.getLogger("MeuLogger")

    def info(self, message):
        if self.use_print:
            print(f"[INFO] {message}")
        else:
            self.logger.info(message)

    def warning(self, message):
        if self.use_print:
            print(f"[WARNING] {message}")
        else:
            self.logger.warning(message)

    def error(self, message):
        if self.use_print:
            print(f"[ERROR] {message}")
        else:
            self.logger.error(message)