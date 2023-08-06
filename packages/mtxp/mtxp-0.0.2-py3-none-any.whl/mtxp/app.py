#!/use/bin/env python3
from subprocess import CompletedProcess
import sys
from pathlib import Path
import os
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
import logging
from .services.tor import startup_tor
import json
import traceback
from flask import Flask,request

from .config import config  # 导入存储配置的字典

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



app = Flask(__name__)
app.config.from_object(config['development'])  # 获取相应的配置类

API_PREFIX = app.config.get("API_PREFIX","/mtpapi")



@app.route(f"{API_PREFIX}")
def hello():
    return "mtp"

@app.route(f"{API_PREFIX}/env")
def api_env():
    items = [{k:os.environ.get(k)} for k in os.environ.keys()]
    return {
        "success": True,
        "data":items
    }

@app.route(f"{API_PREFIX}/start_tor")
def api_start_tor():
    logger.info("api_startup_tor")
    try:
        startup_tor("logs/.tor.log")
        return {"success":True}
    except Exception as unknow:
        # traceback.print_exception(unknow)
        logger.exception(unknow)
        return {
            "success":False,
            "data":str(unknow)
        }

def entry():
    app.run(debug=True, host='0.0.0.0', port=5000)
