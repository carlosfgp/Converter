import logging
import os


class LoggerConverter:

    def logger(self, formatter="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
               debugLevel=logging.DEBUG):

        dirName = os.path.join(os.path.dirname(__file__), "logs")
        log_file = os.path.join(dirName, "converter.log")
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            with open(log_file, "w") as f:
                f.write("Initialization...\n")
        elif os.path.isfile(log_file):
            # Restting log file
            with open(log_file, "w") as f:
                f.write("Initialization...")

        log = logging.getLogger(self)
        log.setLevel(debugLevel)
        formatter = logging.Formatter(formatter)

        # Console log handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(debugLevel)

        # converter.log handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(debugLevel)
        file_handler.setFormatter(formatter)

        log.addHandler(file_handler)
        log.addHandler(console_handler)

        return log
