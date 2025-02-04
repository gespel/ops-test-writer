import json
import logging
import time

logging.basicConfig(
    filename="/var/log/testapp.log",
    level=logging.INFO,
    format="{\"timestamp\": \"%(asctime)s\", \"severity\": \"%(levelname)s\", \"message\": \"%(message)s\"}"
)

logger = logging.getLogger("ops-test-writer")

while(True):
    logger.info("1 second passed...")
    time.sleep(1)