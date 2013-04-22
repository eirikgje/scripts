#!/usr/bin/python

import subprocess
import shlex
import sys
import os

link = sys.argv[1]
outname = sys.argv[2]

#Remove playlist part of link
if '&list' in link:
    link = link[:link.find('&list')]

id = link[link.find('?v=') + 3:]

subprocess.call(shlex.split('youtube-dl %s' % link))
fname = ''.join((id, '.flv'))
if not os.path.exists(fname):
    fname = ''.join((id, '.mp4'))
    if not os.path.exists(fname):
        fname = ''.join((id, '.webm'))
subprocess.call(shlex.split('avconv -i %s "%s"' % (fname, outname)))
subprocess.call(shlex.split('rm ./%s' % fname))
