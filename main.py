import json
import logging
import time

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            "timestamp": self.formatTime(record),
            "severity": record.levelname,  
            "message": record.getMessage()
        }
        return json.dumps(log_message)  

logger = logging.getLogger("ops-test-writer")
logger.setLevel(logging.INFO)  

file_handler = logging.FileHandler("/var/log/testapp.log")
file_handler.setFormatter(JsonFormatter())

logger.addHandler(file_handler)

i = 0

while(True):
    logger.info("10 seconds passed...")
    if i == 3:
        i = 0
        logger.warning("30 seconds passed!")
    time.sleep(10)
    i += 1