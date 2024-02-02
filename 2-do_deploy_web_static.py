#!/usr/bin/python3
""" # 2. Deploy archive! """
from fabric.api import *
from datetime import datetime
import os.path as path


env.hosts = ["34.224.63.137", "100.25.192.100"]
env.user = "ubuntu"

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
    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split('/')[-1]
        remote_path = ("/data/web_static/releases/{}"
                       .format(archive_name.split('.')[0]))
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, remote_path))
        run("rm -f /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}/".format(remote_path, remote_path))
        run("rm -rf {}/web_static".format(remote_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(remote_path))
        return True
    except Exception:
        return False
