#!/usr/bin/python3
"""
Fabric script that distributes an archive to a pair of
web servers, using the function do_deploy.
"""
from fabric.api import *

env.hosts = ['ubuntu@34.139.188.96', 'ubuntu@54.209.148.200']

def def do_deploy(archive_path):
    """
    Function that distributes an archive.
    """
    try:
        with cd("/tmp"):
            put("versions/*.tgz", )
		
		run("mkdir -p versions")
		run(mkdir -p /data/web_static/releases/web_static_20170315003959/)
	    


		
		
		local("mkdir -p versions")
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        compr_file = "versions/web_static_{}.tgz".format(d_t)
        local("tar -cvzf {} web_static".format(compr_file))
        return True
    except:
        return False
