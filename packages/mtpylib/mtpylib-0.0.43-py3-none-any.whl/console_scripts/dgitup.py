import sys
import os
from mtlibs.docker_helper import isInContainer
from mtlibs import process_helper
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
from mtlibs.github import gitup
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


def console_script_entry():
    print("(试验), 直接clone 并启动开发容器", flush=True)
    gitup("https://github.com/codeh007/zappa_cms.git")