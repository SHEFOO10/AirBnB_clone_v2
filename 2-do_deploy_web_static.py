#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os.path as path


env.user = "ubuntu"
env.hosts = ["34.224.63.137", "100.25.192.100"]


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


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if path.exists(archive_path) is False:
        return False
    with cd('/tmp'):
        archive_name = archive_path.split('/')[-1]
        put(f"{archive_path}", f"{archive_name}")
        sudo("tar -xvzf {} -C /data/web_static/releases/".format(archive_name))
        sudo("rm -f {}".format(archive_name))
        sudo("rm -f /data/web_static/current")
        sudo("ln -s /data/web_static/releases/web_static \
/data/web_static/current")
    return True
