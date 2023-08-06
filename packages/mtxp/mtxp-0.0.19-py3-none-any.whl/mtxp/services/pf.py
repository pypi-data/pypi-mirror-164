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
import shutil
from mtlibs import process_helper

import logging
logger = logging.getLogger(__name__)



def startup_pf(lhost,lport,rhost,rport):
    logfile_path = f"logs/pf-{lhost}-{lport}-{rhost}-{rport}.log"
    Path(logfile_path).parent.mkdir(parents=True,mode=0o700, exist_ok=True)
    with open(logfile_path,'w') as logfile:
        logfile.write("=========================  start pf ==================================\n")
        data_dir =join(Path(__file__).parent.parent,"data")
        p = subprocess.Popen(shlex.split(f"node {data_dir}/tun.js {lhost} {lport} {rhost} {rport}"), stdout=logfile, stderr=logfile)



    

