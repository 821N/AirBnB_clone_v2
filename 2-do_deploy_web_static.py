#!/usr/bin/python3
"""
    deploy archive to servers
"""

from fabric.api import *
import os

env.hosts = ["35.231.144.105", "34.74.125.205"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ send files to server """
    archive_name = os.path.basename(archive_path)
    name = archive_name.split(".")[0]
    dest = "/data/web_static/releases/" + name + "/"
    return (
        put(archive_path, "/tmp/" + archive_name).succeeded and
        run("mkdir -p " + dest).succeeded and
        run("tar -xzf /tmp/" + archive_name + " -C " + dest).succeeded and
        run("rm /tmp/"+archive_name).succeeded and
        run("rm /data/web_static/current").succeeded and  # ugh
        run("ln -s " + dest + "/web_static /data/web_static/current").succeeded
    )
