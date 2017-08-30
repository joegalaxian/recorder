#!/usr/bin/env python

import requests
import datetime
import time

# Stream URLs
BLUE = 'http://mp3.metroaudio1.stream.avstreaming.net:7200/bluefmaudio1'
METRO = 'http://mp3.metroaudio1.stream.avstreaming.net:7200/metro'
TIME = 14400 # seconds

# Config
CHUNK_SIZE = 2048 # Bytes
VERBOSE = True

# Colours
RED = '\033[91m'
END = '\033[0m'

# Init varialbes
url = BLUE
t_pre = 0
t_post = 0 
t_start = datetime.datetime.now()
bytes_transferred = 0
timestamp = str(datetime.datetime.now()).replace(' ', '_').replace('-', '').replace('.', '').replace(':', '')	
filename = 'gentesexy_%s.mp3' % timestamp[:15]

r = requests.get(url, stream=True)

print "Recorder by @joegalaxian (c) 2017"
if VERBOSE:
	print '----------------------------------'
	print '[i] CTRL+C to exit'
	print '[i] Output:', filename
	print '[i] Stream:', url

with open(filename, 'wb') as f:
	try:
		for chunk in r.iter_content(CHUNK_SIZE):
			f.write(chunk)
			bytes_transferred += len(chunk)			
			# Status
			t_now = datetime.datetime.now()			
			t_post = time.time()
			status = RED + '\r[*] RECORDING - Elapsed: %s - Speed: %s KB/s - Size: %s KB         ' % (str(t_now - t_start), int((len(chunk)/(t_post-t_pre)/1024)), int(bytes_transferred/1024))
			print status + END + '',
			t_pre = time.time()

			if t_now > datetime.datetime(2017, 8, 30, 2, 0, 0): break
	except KeyboardInterrupt:
		pass
