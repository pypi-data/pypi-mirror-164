import sys
import os

from mtlibs import process_helper

from dotenv import load_dotenv, find_dotenv
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


def console_script_entry():
    print("启动docker开发环境", flush=True)

    print("启动ssh服务")
    process_helper.exec("""service ssh start""")

    print("sleep infinity")
    process_helper.exec("""sleep infinity""")
        