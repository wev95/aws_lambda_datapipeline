import logging
import sys

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('asurion-financial-reconciliation-file-data-pipeline-lambda')
logger.setLevel(logging.INFO)

stream_info = logging.StreamHandler(stream=sys.stdout)
stream_info.setLevel(logging.INFO)
stream_info.setFormatter(formatter)

stream_error = logging.StreamHandler(stream=sys.stderr)
stream_error.setLevel(logging.ERROR)
stream_error.setFormatter(formatter)

logger.addHandler(stream_info)
logger.addHandler(stream_error)