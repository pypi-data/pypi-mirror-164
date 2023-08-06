#!/use/bin/env python3
from subprocess import CompletedProcess
import sys
from pathlib import Path
import os
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
from mtlibs.docker_helper import isInContainer
from .setup_nginx import setup_nginx
from .setup_wordpress import setup_wordpress
from .setup_mtxlib import setup_mtxlib
from .setup_phpfpm import startup_phpfpm
import logging

from flask import Flask
app = Flask(__name__)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def console_script_entry():
    logger.info("sm starting")
    sm_git = os.environ.get("SM_GIT")
    logger.debug(f"sm git value: {sm_git}")

    logger.info("startup sm api service")
    startup_sm_api()

@app.route("/sm/hello")
def hello():
    print("22222")
    return "Hello World!2"

def startup_sm_api():
    app.run(debug=True,host='0.0.0.0', port=5000)