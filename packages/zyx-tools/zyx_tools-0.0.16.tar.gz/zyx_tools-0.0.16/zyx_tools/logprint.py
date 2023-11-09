import os
import time
import sys
from threading import Thread
import logging
from typing import Callable


# 输出unity导出工程的日志
class Tail(Thread):
    def __init__(self, filename, tagname):
        self._filename = filename
        self._stop_reading = False
        self._tagname = tagname
        Thread.__init__(self)

    def run(self, need_stop: Callable[[], bool] = None):
        print(f"{self._tagname} start read")
        while not os.path.exists(self._filename):
            time.sleep(0.1)
        with self.open_default_encoding(self._filename, mode="rb") as file:
            while True:
                if need_stop and need_stop():
                    break
                where = file.tell()
                line = file.readline()
                if self._stop_reading and not line:
                    break
                if not line:
                    time.sleep(1)
                    file.seek(where)
                else:
                    if sys.stdout.closed:
                        return
                    logging.info("[%s]:line.rstrip()", self._tagname)
                    sys.stdout.flush()
        print(f"{self._tagname} stop read")

    def stop(self):
        self._stop_reading = True
        print(f"{self._tagname} stop read")
        # Wait for thread read the remaining log after process quit in 5 seconds
        self.join(5)

    @staticmethod
    def open_default_encoding(file, mode):
        return open(file, mode=mode)
