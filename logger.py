import logging
from config import Config

class Logger:
    def __init__(self):
        logging.basicConfig(filename=Config.LOG_FILE, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def log(self, message, level="info"):
        if level == "info":
            self.logger.info(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "warning":
            self.logger.warning(message)
        else:
            self.logger.debug(message)

    def get_logs(self):
        with open(Config.LOG_FILE, "r") as f:
            return f.read()
