import logging
import os

logging.basicConfig()
logger = logging.getLogger('payment-system')
logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))
