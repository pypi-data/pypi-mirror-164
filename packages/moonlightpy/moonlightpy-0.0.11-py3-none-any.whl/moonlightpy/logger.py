import logging
from datetime import datetime

LOG_FORMAT = "[%(asctime)s][%(levelname)s] %(message)s"
logging.basicConfig(
    filename="moonlight_{}.log".format(datetime.now().strftime("%Y%m%d")),
    level=logging.INFO,
    format=LOG_FORMAT,
)

info = logging.info
debug = logging.debug
warning = logging.warning
error = logging.error
critical = logging.critical
