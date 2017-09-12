#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests

def record(stream_url):
    """Records MP3 from parametered URL stream to 'output.mp3'"""
    r = requests.get(stream_url, stream=True)
    with open('output.mp3', 'wb') as fd:
        for chunk in r.iter_content(1024):
            fd.write(chunk)

if __name__ == '__main__':
    try:
        record(sys.argv[1])
    except:
        print 'ERROR. Usage: python reclite.py <stream_url>'
