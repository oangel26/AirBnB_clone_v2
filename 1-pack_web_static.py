#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder. Use the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function to create a .tgz archive.
    """
    try:
        local("mkdir -p /versions/")
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        compr_file = "versions/web_static_{}.tgz".format(d_t)
        local("tar -cvzf {} web_static".format(compr_file))
        return compr_file
    except:
        return None
