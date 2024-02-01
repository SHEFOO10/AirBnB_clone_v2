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
        # upload archive to remote host
        put(f"{archive_path}", "/tmp/")

        # get archive name
        archive_name = archive_path.split('/')[-1]

        # set path for target directory
        remote_path = "/data/web_static/releases/" + archive_name.split('.')[0]

        # make sure target directory is present
        sudo(f"mkdir -p {remote_path}")

        # extract archive content
        sudo("tar -xvzf /tmp/{} -C {}"
             .format(archive_name, remote_path))

        # delete archive from the remote server
        sudo("rm -f /tmp/{}".format(archive_name))

        # mv content of web_static_datetime/web_static to web_static_datetime
        sudo(f"mv -f {remote_path}/web_static/* {remote_path}/")

        # delete web_static directory
        sudo(f"rm -r {remote_path}/web_static")

        # remove existing link
        sudo("rm -f /data/web_static/current")

        # recreate link
        sudo(f"ln -s /data/web_static/releases/{archive_name.split('.')[0]} \
/data/web_static/current")
        return True
    except Exception:
        return False
