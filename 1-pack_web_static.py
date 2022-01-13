#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder. Use the function do_pack.
"""
from fabric.api import local
from datetime import datetime

def do_pack():
	local("mkdir -p /versions/")
	day =datetime.now().strftime("%Y%m%d%H%m%s")
	compr_file =  "/versions/web_static_{}".format(day)
	local("tar -czf {}.tgz /web_static".format(compr_file))
	try:
		return compr_file
	except: 
		return None
