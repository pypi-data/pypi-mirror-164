#!/use/bin/env python3
# from asyncio import subprocess
import subprocess
from subprocess import CompletedProcess
import sys
from pathlib import Path
import os
from os.path import join
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
from mtlibs.docker_helper import isInContainer
from .setup_nginx import setup_nginx
from . import wordpress_helper
from .setup_mtxlib import setup_mtxlib
from .setup_phpfpm import startup_phpfpm
from datetime import datetime
import logging
import json
from flask import Flask,request
import shlex

from .config import config  # 导入存储配置的字典

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

ENV_FILE = find_dotenv()
if ENV_FILE:
    logger.info(f"找到Env 文件{ENV_FILE}")
    load_dotenv(ENV_FILE)
else:
    logger.info("找不到env文件？")

defaut_env_file = join(os.getcwd(),".env")
logger.info(f"加载默认env file: {defaut_env_file}")
load_dotenv(defaut_env_file)

app = Flask(__name__)
app.config.from_object(config['development'])  # 获取相应的配置类

API_PREFIX = app.config.get("API_PREFIX","/smapi")
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            print("MyEncoder-datetime.datetime")
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        if isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, float):
            return float(obj)
        #elif isinstance(obj, array):
        #    return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

def console_script_entry():
    logger.info("sm starting")
    sm_git = os.environ.get("SM_GIT")
    logger.debug(f"sm git value: {sm_git}")

    logger.info("startup sm api service")
    startup_sm_api()



@app.route(f"{API_PREFIX}/hello")
def hello():
    return "Hello!"


@app.route(f"{API_PREFIX}/setup_nginx")
def api_setup_nginx():
    logger.info("setup_nginx called")
    setup_nginx()
    return {
        "success": True
    }


@app.route(f"{API_PREFIX}/deploy_wordpress")
def deploy_wordpress():
    logger.info("deploy wordpress api called")
    try:
        deployToDir = app.config.get("HTML_ROOT_DIR")
        wordpress_helper.deploy_wordpress(deployToDir)
        startup_phpfpm()
        return {
            "success": True
        }
    except Exception as unknow:
        logger.error(f"deploy_wordpress error {unknow}")
        return {
            "success": False
        }

@app.route(f"{API_PREFIX}/env")
def api_env():
    items = [{k:os.environ.get(k)} for k in os.environ.keys()]
    return {
        "success": True,
        "data":items
    }

def startup_sm_api():
    app.run(debug=True, host='0.0.0.0', port=5000)



def entry_dc():
    items = {k: os.environ.get(k) for k in os.environ.keys()}
    docker_compose_addi_args = items.get("DOCKER_COMPOSE_ARGS","")
    logger.info(f"docker-compose 附加参数:{docker_compose_addi_args}") 
    argv = " ".join(sys.argv[1:])
    cmd = f"docker-compose {docker_compose_addi_args} {argv}"
    logger.info(f"执行命令：{cmd}")
    result2 = subprocess.run(shlex.split(cmd))
    if result2.returncode != 0:
        logger.error(f"exec with error {result2}")
