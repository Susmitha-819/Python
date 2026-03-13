import logging
import sys

logger=logging.getLogger('package')
handler=logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
logger.warning('This is a warning message to stdout')

