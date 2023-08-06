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
from .services.pf import startup_pf
import json
import traceback
from flask import Flask, request
import subprocess
import traceback
import shlex
import requests
import click
from flask import Flask
from flask.cli import with_appcontext

import yaml
from .config import config  # 导入存储配置的字典

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


data_dir = join(Path(__file__).parent, "data")

app = Flask(__name__)
app.config.from_object(config['development'])  # 获取相应的配置类

API_PREFIX = app.config.get("API_PREFIX", "/mtpapi")


@app.route(f"{API_PREFIX}")
def home():
    return "mtxp"


@app.route(f"{API_PREFIX}/env")
def api_info():
    items = [{k: os.environ.get(k)} for k in os.environ.keys()]
    return {
        "success": True,
        "data": {
            "env": items,
            "__file__": __file__
        }
    }


@app.route(f"{API_PREFIX}/start_tor")
def api_start_tor():
    logger.info("api_startup_tor")
    try:
        startup_tor("logs/.tor.log")
        return {"success": True}
    except Exception as unknow:
        # traceback.print_exception(unknow)
        logger.exception(unknow)
        return {
            "success": False,
            "data": str(unknow)
        }


@app.route(f"{API_PREFIX}/start_openvpn")
def api_start_openvpn():
    """openvpn 功能未完成, 目前也用不上"""
    logger.info("api_startup_openvpn")
    logger.info("openvpn 功能未完成，原因是打包时,ta.key文件不知道为什么打包不进去。")
    try:
        startup_openvpn("logs/.openvpn.log")
        return {"success": True}
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success": False,
            "data": str(unknow)
        }

@app.route(f"{API_PREFIX}/start_clash")
def api_start_clash():
    logger.info("api_start_clash")
    try:
        startup_clash("logs/.clash.log")
        return {"success": True}
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success": False,
            "data": str(unknow)
    }


@app.route(f"{API_PREFIX}/start_mtxtun")
def api_start_mtxtun():
    logger.info("api start_mtxtun")
    try:
        startup_mtxtun("logs/.mtxtun.log")
        return {"success": True}
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success": False,
            "data": str(unknow)
        }


@app.route(f"{API_PREFIX}/start_pf")
def api_start_pf():
    """旧的mtxtun端口加密转发改版"""
    logger.info("api start_mtxtun2")
    try:
        # 加载配置
        yaml_content = None
        with open(join(data_dir, "mtxtun.yml"), 'r', encoding="utf-8") as f:
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        pf_items = yaml_content["pf"]["items"]
        # 启动端口转发
        for item in pf_items:
            startup_pf(item["lhost"],item["lport"],item["rhost"],item["rport"])
        return {"success": True,
                "data": pf_items
            }
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success": False,
            "data": str(unknow)
        }

@app.route(f"{API_PREFIX}/tun_config")
def api_tun_config():
    try:
        with open(join(data_dir, "mtxtun.yml"), 'r', encoding="utf-8") as f:
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
            return {
                "success": True,
                "data": yaml_content
            }
    except Exception as unknow:
        logger.exception(unknow)
        return {
            "success": False,
            "data": str(unknow)
        }


@click.command()
def cli():
    logger.info("cli command")
    print("cli command")

@app.cli.command("hello_command")
@click.argument("ccurl")
@with_appcontext
def entry_agent(ccurl):
    """本地代理入口"""
    ccurl = sys.argv[1]
    if ccurl:
        logger.info(f" 启动参数: {sys.argv} ")
        logger.info(f"ccurl : {ccurl}")
        logger.info(f"作为agent运行")
        def initAgent():
            config_url = f"{ccurl}/mtxpapi/tun_config"
            logger.info(f"config_url {config_url}")
            x = requests.get(config_url)
            jsonData= x.json()
            logger.info(f"配置数据 {jsonData}")
            # logger.info(f"启动端口转发")
            pf_items = jsonData["data"]["pf"]["items"]
            for item in pf_items:
                logger.info(f"启动一个端口转发 {item}")
                startup_pf(item.rhost,item.rport,item.lhost, item.lport)

        initAgent()
        app.run(debug=True, host='0.0.0.0', port=5500)

def entry():
    """默认入口"""
    if len(sys.argv) >= 2:
        entry_agent
    else:
        app.run(debug=True, host='0.0.0.0', port=5000)
