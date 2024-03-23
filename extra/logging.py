import sys

from loguru import logger
logger.debug("That's it, beautiful and simple logging!")
logger.add(sys.stderr, format="{time} {level}{message}", filter="my_module", level="INFO")
logger.add("file_1.log", rotation="500 MB")