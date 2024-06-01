import logging

epsa_logger = logging.getLogger("epsa_wizard")

epsa_logger.setLevel(logging.DEBUG)

# File handler, DEBUG
fh_debug = logging.FileHandler("epsa_debug.log", mode="w+")
fh_debug.setLevel(logging.DEBUG)

# File handler, INFO
fh_info = logging.FileHandler("epsa_info.log", mode="w+")
fh_info.setLevel(logging.INFO)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Formatter
formatter_file = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(funcName)s - %(threadName)s\n\t-> %(message)s"
)
formatter_console = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(funcName)s - %(threadName)s"
)

# Set formatter
fh_debug.setFormatter(formatter_file)
fh_info.setFormatter(formatter_file)
ch.setFormatter(formatter_console)

# Add handlers to logger
epsa_logger.addHandler(fh_debug)
epsa_logger.addHandler(fh_info)
epsa_logger.addHandler(ch)
