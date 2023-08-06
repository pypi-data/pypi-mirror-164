#!/use/bin/env python3
from subprocess import CompletedProcess
import sys
from pathlib import Path
import os
from os.path import join
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
import logging
import json
import traceback
from flask import Flask, request
import subprocess
import traceback
import shlex
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

API_PREFIX = app.config.get("API_PREFIX", "/mtxagent")


@app.route(f"{API_PREFIX}")
def home():
    return "mtxp_agent"


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

def entry():
    app.run(debug=True, host='0.0.0.0', port=5500)
