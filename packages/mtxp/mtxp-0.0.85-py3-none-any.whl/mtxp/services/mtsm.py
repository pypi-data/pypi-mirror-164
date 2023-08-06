#!/usr/bin/env python3
import sys
import os
from os.path import join
import subprocess
from pathlib import Path
import time
import subprocess
import traceback
import shlex
from .. import settings
from os import path
import threading
import logging

logger = logging.getLogger(__name__)


class MtsmService():
    # _instance_lock = threading.Lock()
    def __init__(self):
        self.logdirBase = settings.get("LOG_DIR")

    def write_log(self, message: str):
        self.logfile.write(f"{message}\n")
        self.logfile.flush()

    def start(self):    
        self.thread.start()

    def thread_start(self):
        logger.info("启动mtsm")

        self.target_process = subprocess.Popen(shlex.split(f"mtsm"),
                            stdout=self.logfile,
                            stderr=self.logfile)

    