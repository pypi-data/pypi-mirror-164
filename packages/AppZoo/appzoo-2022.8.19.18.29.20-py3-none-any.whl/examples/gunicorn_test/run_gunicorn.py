#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : run_gunicorn
# @Time         : 2019-11-21 14:39
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import re
import sys

from gunicorn.app.wsgiapp import run

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())
# python3 run_gunicorn.py  -w 4 -b 0.0.0.0:5000 main:app