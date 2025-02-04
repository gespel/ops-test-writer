import json
import logging
import time
import google.cloud.logging

#client = google.cloud.logging.Client()
#client.setup_logging()

logging.basicConfig(
    filename="/var/log/testapp.log",
    level=logging.INFO,
    format="{\"timestamp\": \"%(asctime)s\", \"severity\": \"%(levelname)s\", \"message\": \"%(message)s\"}"
)

logger = logging.getLogger("ops-test-writer")

i = 0

while(True):
    logger.info("10 seconds passed...")
    if i == 3:
        i = 0
        logger.warning("30 seconds passed!")
    time.sleep(10)
    i += 1