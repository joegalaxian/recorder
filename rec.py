#!/usr/bin/env python

import requests
import time
import sys
import datetime

DELAY = 30

def exit_time(timeout, start_time):
	return timeout and timeout <= (time.time() - start_time)

def rec(stream_url, timeout=None):
	print '[*] Stream: %s' % stream_url
	start_time = time.time()

	#filename = 'save/gentesexy_%s_%d.mp3' % (time.strftime('%H%M%S', time.gmtime(time.time())), start_time) # gentesexy_105959_654321.mp3
	filename = 'save/gentesexy_%s.mp3' % str(datetime.datetime.now())[:19].replace(' ','_').replace('-','').replace(':','') # gentesexy_20171218_225959.mp3

	f = open(filename, 'wb')
	print '[*] Output: %s' % filename

	while not exit_time(timeout, start_time):
		try:
			print '[*] Connecting stream ...'
			r = requests.get(stream_url, stream=True, timeout=9)

			print '[*] Saving stream ... '
			for chunk in r.iter_content(1024):
				f.write(chunk)

				bold_text = "\033[1m"
				reset_text = "\033[0;0m"
				recorded_time = time.strftime('%H:%M:%S', time.gmtime(int(time.time() - start_time))) # 'HH:MM:SS'
				print '\r' + bold_text + '[*] REC ' + recorded_time + reset_text,
				sys.stdout.flush()

				if exit_time(timeout, start_time): break

		except Exception as e:
			print '\n[!] Error:', e
			print '[*] Retrying in %d seconds ...' % DELAY
			time.sleep(DELAY)

			pass

	f.close()
	print '\n[*] Program terminated.'


if __name__ == '__main__':
	try:
		# python rec.py <stream_url> <timeout>
		s = sys.argv[1]
		t = sys.argv[2]
		#s = 'http://mp3.metroaudio1.stream.avstreaming.net:7200/bluefmaudio1' # Blue FM

		rec(s, timeout=int(t))
	except Exception:
		print '''Usage: python rec.py <stream_url> <timeout>
Fow example: python rec.py http://mp3.metroaudio1.stream.avstreaming.net:7200/bluefmaudio1 15000'''
