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
from .. import settings
from os import path
import threading
import yaml
import logging

logger = logging.getLogger(__name__)


class PfService():
    def __init__(self):
        pass


    def start(self):
        try:
            data_dir = settings.get("DATA_DIR") 
            # 加载配置
            f = open(join(data_dir, "mtxtun.yml"), 'r', encoding="utf-8")
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
           
            pf_items = yaml_content["pf"]["items"]
            # 启动端口转发
            for item in pf_items:
                self.portforward_x(item["lhost"],item["lport"],item["rhost"],item["rport"])
            return {"success": True,
                    "data": pf_items
                }
        except Exception as unknow:
            logger.exception(unknow)
            return {
                "success": False,
                "data": str(unknow)
            }

    def portforward_x(self, lhost, lport, rhost, rport):
        """单个加密端口转发"""
        logfile_path = f"logs/pf-{lhost}-{lport}-{rhost}-{rport}.log"
        Path(logfile_path).parent.mkdir(
            parents=True, mode=0o700, exist_ok=True)
        with open(logfile_path, 'w') as logfile:
            logfile.write(
                "=========================  start pf ==================================\n")
            data_dir = join(Path(__file__).parent.parent, "data")
            p = subprocess.Popen(shlex.split(
                f"node {data_dir}/tun.js {lhost} {lport} {rhost} {rport}"), stdout=logfile, stderr=logfile)
