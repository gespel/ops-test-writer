import json
import logging
import time


def old_mock_log():
    class JsonFormatter(logging.Formatter):
        def format(self, record):
            log_message = {
                "app": "emsctrl",
                "timestamp": self.formatTime(record),
                #"logging.googleapis.com/severity": record.levelname,
                "old_severity": "info2",
                "message": record.getMessage()
            }
            return json.dumps(log_message)  

    logger = logging.getLogger("ops-test-writer")
    logger.setLevel(logging.INFO)  

    file_handler = logging.FileHandler("/var/log/testapp.log")
    #file_handler.setFormatter(JsonFormatter())

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

def create_mock_log(appname,
                    category, 
                    index, 
                    level, 
                    logversion, 
                    message, 
                    message_orig, 
                    origin, 
                    pid, 
                    srcfile, 
                    srcline, 
                    target, 
                    timestamp, 
                    trans):
    log_message = {
        "app": appname,
        "category": category,
        "index": index,
        "level": level,
        "logversion": logversion,
        "message": message,
        "message_orig": message_orig,
        "origin": origin,
        "pid": pid,
        "srcfile": srcfile,
        "srcline": srcline,
        "target": target,
        "timestamp": timestamp,
        "trans": trans
    }
    return json.dumps(log_message)

def mock():
    import random
    import time

    m1 = {"app":"bovprx","category":"T_APP","index":"events","level":"warning","logversion":1,"message":"CAliveTopicMsgSink::tryRecoveryOnMissingAlive Letzte Aktualisierungsnachricht erst 1800 sek her. PseudoDzaGenerierung wird nicht durchgefuehrt.","message_orig":"CAliveTopicMsgSink::tryRecoveryOnMissingAlive Letzte Aktualisierungsnachricht erst 1800 sek her. PseudoDzaGenerierung wird nicht durchgefuehrt.","origin":"trace","pid":21166,"srcfile":"db/bov/prx/CBovAktMgr.cpp","srcline":90,"target":"ext","timestampx":"2025-01-28T14:42:20.655Z","trans":"notInitialized"}
    m2 = {"app":"pdbnafarc","category":"T_APP_PDBNAF","index":"events","level":"info","logversion":1,"message":"Datenbank arcdb wird nachgefuehrt, letzte SeqNum 27273396","message_orig":"Datenbank arcdb wird nachgefuehrt, letzte SeqNum 27273396","origin":"trace","pid":21978,"srcfile":"pdb/naf/prg/CPdbNafMgr.cpp","srcline":587,"target":"int","timestampx":"2025-01-28T14:42:24.448Z","trans":"notInitialized"}
    m3 = {"app":"pdbnaf","category":"T_APP_PDBNAF","index":"events","level":"info","logversion":1,"message":"Datenbank psudb wird nachgefuehrt, letzte SeqNum 699386198","message_orig":"Datenbank psudb wird nachgefuehrt, letzte SeqNum 699386198","origin":"trace","pid":21974,"srcfile":"pdb/naf/prg/CPdbNafMgr.cpp","srcline":587,"target":"int","timestampx":"2025-01-28T14:42:24.451Z","trans":"notInitialized"}
    m4 = {"app":"emsctrl","category":"T_SYSCTRL_HTTP","index":"events","level":"info","logversion":1,"message":"GET /metrics 404","message_orig":"GET /metrics 404","origin":"trace","pid":17299,"srcfile":"bas/sct/ctrl/CHTTPRequestHandler.cpp","srcline":72,"target":"int","timestampx":"2025-01-28T14:42:27.221Z","trans":"notInitialized"}
    m5 = {"app":"bovprx","category":"T_BOV_UPD","index":"events","level":"warning","logversion":1,"message":"Alive vom Bov-Publisher fehlt","message_orig":"Alive vom Bov-Publisher fehlt","origin":"trace","pid":21166,"srcfile":"db/bov/prx/CBovAktMgr.cpp","srcline":80,"target":"ext","timestampx":"2025-01-28T14:42:50.659Z","trans":"notInitialized"}
    
    messages = [json.dumps(m1), json.dumps(m2), json.dumps(m3), json.dumps(m4), json.dumps(m5)]

    while True:
        with open("/var/log/testapp.log", "a") as f:
            m = messages[random.randint(0, 4)]
            print(f"Writing log: {m}")
            f.write(m + "\n")
        time.sleep(5)

mock()