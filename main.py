import json
import logging
import time

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            "logName": "TestApp",
            "timestamp": self.formatTime(record),
            "logging.googleapis.com/severity": "info",
            "message": record.getMessage()
        }
        return json.dumps(log_message)  

logger = logging.getLogger("ops-test-writer")
logger.setLevel(logging.INFO)  

file_handler = logging.FileHandler("/var/log/testapp.log")
file_handler.setFormatter(JsonFormatter())

logger.addHandler(file_handler)

i = 1

while(True): 
    if i % 3 == 0:
        i = 0
        logger.warning("30 seconds passed!")
    else:
        logger.info("10 seconds passed...")
    time.sleep(10)
    i += 1