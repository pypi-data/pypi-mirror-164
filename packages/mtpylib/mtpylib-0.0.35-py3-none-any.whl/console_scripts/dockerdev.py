import sys
import os
from mtlibs.docker_helper import isInContainer
from mtlibs import process_helper
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


def console_script_entry():
    print("启动docker开发环境", flush=True)

    if not isInContainer():
        print("本部署脚本仅在docker 容器内有效")

    print("启动ssh服务")
    process_helper.exec("""service ssh start""")


    print("启动项目内置启动脚本")

    if Path(".vscode/bin/docker_dev").exists():
        cp_docker_dev = process_helper.exec("""bash .vscode/bin/docker_dev""")
        if cp_docker_dev.check_returncode !=0:
            print("内置启动脚本执行错误")

    print("sleep infinity")
    process_helper.exec("""sleep infinity""")
