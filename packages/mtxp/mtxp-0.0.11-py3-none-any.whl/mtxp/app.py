#!/use/bin/env python3
from subprocess import CompletedProcess
import sys
from pathlib import Path
import os
from os.path import join
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
import logging
from .services.tor import startup_tor
from .services.openvpn import startup_openvpn
from .services.clash import startup_clash
from .services.mtxtun import startup_mtxtun
import json
import traceback
from flask import Flask,request

import yaml
from .config import config  # 导入存储配置的字典

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


data_dir =join(Path(__file__).parent,"data")

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

@app.route(f"{API_PREFIX}/start_mtxtun")
def api_start_mtxtun():
    logger.info("api start_mtxtun")
    try:
        startup_mtxtun("logs/.mtxtun.log")
        return {"success":True}
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success":False,
            "data":str(unknow)
        }

@app.route(f"{API_PREFIX}/tun_config")
def api_tun_config():
    try:
        with open(join(data_dir,"mtxtun.yml"),'r', encoding="utf-8") as f:
            yaml_content = yaml.load(f,Loader=yaml.FullLoader)
            return {
                "success":True,
                "data":yaml_content
            }
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success":False,
            "data":str(unknow)
        }
def entry():
    app.run(debug=True, host='0.0.0.0', port=5000)
