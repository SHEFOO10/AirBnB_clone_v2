#!/usr/bin/python3
""" fabric tasks """
from fabric.api import *
from datetime import datetime


def do_pack():
    """
        compress web_static directory to tar archive
    """
    local("mkdir -p versions")
    pack_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/" + "web_static_" + pack_datetime + ".tgz"
    result = local("tar -cvzf {} web_static".format(path))
    if result.succeeded:
        return path
    else:
        return None
