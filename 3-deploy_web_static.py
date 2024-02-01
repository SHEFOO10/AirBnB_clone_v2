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
    try:
        archive_name = archive_path.split('/')[-1]
        remote_path = "/data/web_static/releases/" + archive_name.split('.')[0]
        put(f"{archive_path}", "/tmp/")
        run(f"mkdir -p {remote_path}")
        run("tar -xvzf /tmp/{} -C {}"
            .format(archive_name, remote_path))
        run("rm -f /tmp/{}".format(archive_name))
        run(f"mv {remote_path}/web_static/* {remote_path}/")
        run(f"rm -rf {remote_path}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{archive_name.split('.')[0]} \
/data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    path = do_pack()
    if path is False:
        return False
    if do_deploy(path) is False:
        return False
    return True
