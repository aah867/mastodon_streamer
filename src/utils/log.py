import logging
from logging.handlers import QueueHandler

########################################
# Setup Logging with desired log-level
########################################

LOG_FILENAME = 'app.log'
log = logging.getLogger('Logger')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20000000, backupCount=5)
handler.setFormatter(formatter)
log.addHandler(handler)
