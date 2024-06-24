import logging
from logging.config import fileConfig

fileConfig('logging_config.ini',
           disable_existing_loggers=False)
logger = logging.getLogger('a')
logger.debug('hello world')
logger.info(logger.level)
logger.warning(logger.name)
