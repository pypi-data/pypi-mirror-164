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
import logging

logger = logging.getLogger(__name__)

class TorService():
    def __init__(self):
        pass
    def start(self):
        logdirBase = settings.get("LOG_DIR")
        logfile_path = path.join(logdirBase, ".tor.log")
        def thread_start():
            torcc = [
                "VirtualAddrNetworkIPv4 10.192.0.0/10",
                "AutomapHostsOnResolve 1",
                "AvoidDiskWrites 1",
                "SocksPort 0.0.0.0:9050",
                "TransPort 127.0.0.1:9040",
                "DNSPort 127.0.0.1:5353",
                "CookieAuthentication 1",
                "ControlPort 0.0.0.0:9051",
                "HashedControlPassword 16:E600ADC1B52C80BB6022A0E999A7734571A451EB6AE50FED489B72E3DF",
                "HiddenServiceDir /tmp/hidden",
                "HiddenServicePort 80 127.0.0.1:80",
                "HiddenServicePort 22 127.0.0.1:22",
                "HiddenServicePort 443 127.0.0.1:443"
            ]
            # 使用外部代理链接tor网络。
            TOR_SOCKS5PROXY = os.environ.get("TOR_SOCKS5PROXY")
            if TOR_SOCKS5PROXY:
                torcc.append(f"Socks5Proxy {TOR_SOCKS5PROXY}")

            torcc_path = "/tmp/torcc"
            Path(torcc_path).touch(mode=0o700)

            torcc_content = "\n".join(torcc)
            # print(torcc_content)
            with open(torcc_path,"w") as f:
                f.write(torcc_content)

            # logfile_path = logfile
            Path(logfile_path).parent.mkdir(parents=True,mode=0o700, exist_ok=True)
            with open(logfile_path,'w') as logfile:
                logfile.write("=========================  start tor ==================================\n")
                p = subprocess.Popen(shlex.split(f"tor -f {torcc_path}"), stdout=logfile, stderr=logfile)

        thread = threading.Thread(target=thread_start)
        thread.start()

        

