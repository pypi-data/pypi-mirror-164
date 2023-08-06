#!/use/bin/env python3
from subprocess import CompletedProcess
import sys
from pathlib import Path
import os
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
import logging
from .services.tor import startup_tor
from .services.openvpn import startup_openvpn
from .services.clash import startup_clash
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
def home():
    return "mtxp"

@app.route(f"{API_PREFIX}/env")
def api_info():
    items = [{k:os.environ.get(k)} for k in os.environ.keys()]
    return {
        "success": True,
        "data":{
            "env":items,
            "__file__":__file__
        }
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


@app.route(f"{API_PREFIX}/start_openvpn")
def api_start_openvpn():
    """openvpn 功能未完成, 目前也用不上"""
    logger.info("api_startup_openvpn")
    logger.info("openvpn 功能未完成，原因是打包时,ta.key文件不知道为什么打包不进去。")
    try:
        startup_openvpn("logs/.openvpn.log")
        return {"success":True}
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success":False,
            "data":str(unknow)
        }

@app.route(f"{API_PREFIX}/start_clash")
def api_start_clash():
    logger.info("api_start_clash")
    try:
        startup_clash("logs/.clash.log")
        return {"success":True}
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success":False,
            "data":str(unknow)
        }

def entry():
    app.run(debug=True, host='0.0.0.0', port=5000)
