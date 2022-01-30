#!/usr/bin/python3
"""
Fabric script that distributes an archive to a pair of
web servers, using the function do_deploy.
"""
from fabric.api import run, put, env, local
import os
from datetime import datetime

env.hosts = ['34.139.237.222', '174.129.81.127']
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'


def deploy():
    """Fabric script that creates and distributes an archive
    to your web servers, using the function deploy"""

    tgz_file = do_pack()
    if tgz_file is None:
        return False
    do_deploy_value = do_deploy(tgz_file)
    return do_deploy_value


def do_pack():
    """
    Function to create a .tgz archive.
    """
    try:
        local("mkdir -p versions")
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        compr_file = "versions/web_static_{}.tgz".format(d_t)
        local("tar -cvzf {} web_static".format(compr_file))
        return compr_file
    except:
        return None


def do_deploy(archive_path):
    """
    Function that distributes an archive.
    """
    name_dir = archive_path[9:-4]
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name_dir))
        run("sudo tar -xzf /tmp/{}.tgz -C \
        /data/web_static/releases/{}/".format(name_dir, name_dir))
        run("sudo rm /tmp/{}.tgz".format(name_dir))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".
            format(name_dir, name_dir))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(name_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name_dir))
        print("New version deployed!")
        return True
    else:
        return False