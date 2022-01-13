#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder. Use the function do_pack.
"""

def do_pack():

	run("NOWT=$(date +"%F %T")")
	run("/versions/web_static_$NOW.tar.gz /web_static")
