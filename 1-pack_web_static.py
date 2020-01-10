#!/usr/bin/python3
"""
    1
"""

from fabric.api import local
from datetime import datetime
from os import mkdir


def do_pack():
    """ compress web_static """
    try:
        mkdir("versions")
    except:
        pass
    path = datetime.now().strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
    r = local("tar -c -f " + path + " -vz web_static")
    if not r.failed:
        return path
