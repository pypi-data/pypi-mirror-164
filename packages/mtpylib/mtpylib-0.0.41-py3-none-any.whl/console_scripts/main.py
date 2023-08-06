from subprocess import CompletedProcess
import sys
from pathlib import Path
from mtlibs import process_helper
from dotenv import load_dotenv, find_dotenv
from mtlibs.docker_helper import isInContainer
from .setup_nginx import setup_nginx
from .setup_wordpress import setup_wordpress
from .setup_mtxlib import setup_mtxlib
from .setup_phpfpm import startup_phpfpm
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# 入口
def console_script_entry():
    print("命令行参数", sys.argv)
    if not isInContainer():
        print("本部署脚本仅在docker 容器内有效")
    else:        
        # start_django()
        setup_nginx()        
        # setup_wordpress()
        print("启动php-fpm")
        startup_phpfpm()
        # print("启动django 应用")
        # django_dev_cp = process_helper.exec("./manage.py runserver 0.0.0.0:8000 &")
        # if django_dev_cp.returncode == 0:
        #     print("django （开发板）启动成功")
        # setup_mtxlib() 

def start_django():
    print("以gunicorn的方式启动django")
    cmd="""gunicorn mtxcms.wsgi --bind=0.0.0.0:8000 --daemon"""
    cp: CompletedProcess = process_helper.exec(cmd)
    if cp.returncode == 0:
        print("gunicorn成功启动")
    else:
        print("gunicorn启动失败")