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
import logging
logger = logging.getLogger(__name__)



def startup_clash(logfile_path:str):
    Path(logfile_path).parent.mkdir(parents=True,mode=0o700, exist_ok=True)
    with open(logfile_path,'w') as logfile:
        logfile.write("=========================  start openvpn ==================================\n")
        logger.info("start openvpn")
        logger.debug(f"__file__ : {__file__}")
        logger.debug(f"__package__: {__package__}")

        data_dir =join(Path(__file__).parent.parent,"data")
        logger.debug(f"data dir: {data_dir}")
        # shutil.copytree(join(data_dir,'openvpn'), "/etc/openvpn/", dirs_exist_ok=True)
        # openvpn_config = "abc"
        p = subprocess.Popen(shlex.split(f"clash -f {data_dir}/clash/config.yaml"), stdout=logfile, stderr=logfile)



    

