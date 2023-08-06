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
import logging
logger = logging.getLogger(__name__)


LOG_FILE=".openvpn.log"

def startup_openvpn(logfile_path:str):
    Path(logfile_path).parent.mkdir(parents=True,mode=0o700, exist_ok=True)
    with open(logfile_path,'w') as logfile:
        logfile.write("=========================  start openvpn ==================================")
        logger.info("start openvpn")
        logger.debug(f"__file__ : {__file__}")
        openvpn_config = "abc"
        p = subprocess.Popen(shlex.split(f"openvpn -c {openvpn_config}"), stdout=logfile, stderr=logfile)



    

