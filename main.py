import json
import logging
import time

logging.basicConfig(
    filename="/var/log/oop-test.log",
    level=logging.INFO,
    format="{\"timestamp\": \"%(asctime)s\", \"severity\": \"%(levelname)s\", \"message\": \"%(message)s\"}"
)

logger = logging.getLogger("oop-test-writer")

while(True):
    logger.info("1 second passed...")
    time.sleep(1)