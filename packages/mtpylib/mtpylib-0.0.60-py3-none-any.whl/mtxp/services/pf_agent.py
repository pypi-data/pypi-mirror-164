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
import requests
logger = logging.getLogger(__name__)


class PfClientAgent():
    def __init__(self, serverUrl: str):
        self.serverUrl = serverUrl
        self.logDirBase = settings.get("LOG_DIR")

    def start(self):
        logger.info("PfClientAgent start.")
        config_url = f"{self.serverUrl}/mtxp/tun_config"
        logger.info(f"config_url {config_url}")
        x = requests.get(config_url)
        jsonData = x.json()
        logger.info(f"配置数据 {jsonData}")
        pf_items = jsonData["data"]["pf"]["items"]
        for item in pf_items:
            logger.info(f"(TODO)启动一个端口转发 {item}")
            self.portforward_x(item["rhost"], item["rport"],
                               item["lhost"], item["lport"])
            # startup_pf(item["rhost"],item["rport"],item["lhost"], item["lport"])
        # try:
        #     # data_dir = settings.get("DATA_DIR")
        #     # # 加载配置
        #     # f = open(join(data_dir, "mtxtun.yml"), 'r', encoding="utf-8")
        #     # yaml_content = yaml.load(f, Loader=yaml.FullLoader)

        #     # pf_items = yaml_content["pf"]["items"]
        #     # 启动端口转发
        #     for item in self.config.items:
        #         self.portforward_x(item["lhost"],item["lport"],item["rhost"],item["rport"])

        # except Exception as unknow:
        #     logger.exception(unknow)

    def portforward_x(self, lhost, lport, rhost, rport):
        """单个加密端口转发"""
        logfile_path = f"{self.logDirBase}/pf-{lhost}-{lport}-{rhost}-{rport}.log"
        Path(logfile_path).parent.mkdir(
            parents=True, mode=0o700, exist_ok=True)
        with open(logfile_path, 'w') as logfile:
            logfile.write(
                "=========================  start pf ==================================\n")
            data_dir = join(Path(__file__).parent.parent, "data")
            logger.info(f"data dir 1: {data_dir}")

            data_dir2 = Path(__file__).parent.parent.joinpath("data")
            logger.info(f"data_dir2 : {data_dir2}")

            jsScriptPath = Path(__file__).parent.parent.joinpath(
                "data").joinpath("tun.js")
            logger.info(f"jsScriptPath : {jsScriptPath}")

            jsScriptPath = jsScriptPath.replace("\\","\\\\")
            subprocess.Popen(shlex.split(
                f"node {jsScriptPath} {lhost} {lport} {rhost} {rport}"),
                stdout=logfile,
                stderr=logfile
            )
