

'''
	This is the scan process starter.
'''

'''
	steps:
		1. 	A scan process is started.
			1. the scan process has a flask (a.k.a. keg or reservoir) server built in.
		
		2. 	A request is sent to the scan process to run checks found
			in a path.
		
		3. 	The returns (status and stats) of the scan process are returned.
'''

from botanist.ports.find_an_open_port import find_an_open_port
import botanist.processes.multiple as multi_proc

import body_scan.processes.scan.path as SCAN_path
	
import sys
import json
def ATTEMPT_TAP_keg (
	module_paths
):
	PORT = find_an_open_port ()
	SCAN_PROCESS_path = SCAN_path.FIND ()

	details = json.dumps ({ "module_paths": sys.path })
	process_string = f'''python3 { SCAN_PROCESS_path } keg OPEN --port { PORT } --details \'{ details }\' '''

	procs = multi_proc.start (
		processes = [{
			"string": process_string,
			"CWD": None
		}]
	)

	return [ PORT, procs ]

def start (
	path,
	module_paths = [],
	relative_path = False,
	records = 0
):
	[ PORT, procs ] = ATTEMPT_TAP_keg (
		module_paths
	)
	
	import time
	time.sleep (0.5)
	
	REQUEST_ADDRESS = f'http://127.0.0.1:{ PORT }'
	
	import json
	import requests
	r = requests.put (
		REQUEST_ADDRESS, 
		data = json.dumps ({ 
			"FINDS": [ str (path) ],
			"MODULE paths": module_paths,
			"RELATIVE path": relative_path
		})
	)
	
	def format_response (TEXT):
		import json
		return json.loads (TEXT)
	
	status = format_response (r.text)

	if (records >= 2):
		print ()
		print ("request address:", REQUEST_ADDRESS)
		print ("request status:", r.status_code)
		print ("request text:", json.dumps (status, indent = 4))
		print ()


	exit = procs ["exit"]
	processes = procs ["processes"]
	
	return [ status ]