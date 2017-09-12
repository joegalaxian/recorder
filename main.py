#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import recorder

if __name__ == '__main__':
	# Parse arguments
	if '-h' in sys.argv:
		print '''
rec, version 5.0

usage: rec <url> [-h] [-t <timeout>] [-o <output>] [-v]

  <url>        (required) : stream URL
  -h           (optional) : prints this help message
  -o <output>  (optional) : output filename, 'YYYYMMDD_hhmmss.mp3' by default
  -t <timeout> (optional) : timeout in seconds, indefinitely by default
  -v           (optional) : verbose mode'''
		sys.exit(0)

	try:
		url = sys.argv[1]
	except:
		print 'What URL do you want to record?'
		sys.exit(1)

	try: timeout = int(sys.argv[sys.argv.index('-t') + 1])
	except: timeout = None

	try: output = sys.argv[sys.argv.index('-o') + 1]
	except: output = None

	try: verbose = '-v' in sys.argv
	except: verbose = False

	try:
		# Call main function
		recorder.record(url, timeout=timeout, output=output, verbose=verbose)
	except KeyboardInterrupt:
		pass
