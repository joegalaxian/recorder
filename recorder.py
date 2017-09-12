#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import requests
import sys
import time

def record(stream_url, **kwargs):
	"""
	Records from a mp3 stream URL to a file.
	@params:
		stream_url	- Required : Stream URL.
		output		- Optional : Output filename. Default value: 'YYYYMMDD_hhmmss.mp3'
		timeout		- Optional : Timeout in seconds. If no specified, it will record undefinetely (until execution is interrupted with CTRL+C).
		verbose		- Optional : Bool value 
	"""

	def size_fmt(num):
		for unit in ['','KB','MB','GB','TB','PB','EB','ZB']:
			if abs(num) < 1024.0:
				return '%3.1f%s   ' % (num, unit)
			num /= 1024.0
		return '%.1f%s   ' % (num, 'YB')

	try:
		output = kwargs['output']
		if not output:
			raise Exception
		output += str(datetime.datetime.now())[:19].replace(' ','_').replace('-','').replace(':','') + '.mp3'
	except:
		output = str(datetime.datetime.now())[:19].replace(' ','_').replace('-','').replace(':','') + '.mp3'

	try: timeout = int(kwargs['timeout'])
	except: timeout = None

	try: verbose = (kwargs['verbose'] in (True, 'True', 1))
	except: verbose = False

	if verbose:
		print 'rec v5 by @joegalaxian (c) 2017'
		print '-------------------------------'
		print '[i] CTRL+C to exit'
		print '[i] Stream :', stream_url
		print '[i] Output :', output
		print '[i] Timeout:', timeout

	chunk_size = 1024
	r = requests.get(stream_url, stream=True)
	with open(output, 'wb') as fd:
		try:
			t0 = time.time()
			size = 0
			for chunk in r.iter_content(chunk_size):
				fd.write(chunk)
				if verbose:
					# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
					size += len(chunk)
					progress = '\r%s[*] RECORDING - %s - %s%s' % ('\033[91m', time.strftime('%H:%M:%S', time.gmtime(int(time.time() - t0))), size_fmt(size), '\033[0m')
					print progress,
					sys.stdout.flush()
				if timeout and timeout <= (time.time() - t0): break
		except KeyboardInterrupt:
			print ''
			pass

if __name__ == '__main__':
	# Ignore standalone execution
	pass
