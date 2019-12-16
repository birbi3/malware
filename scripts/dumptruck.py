#!/usr/bin/env python

#standard lib
import os
import subprocess
import re

def main():
	file_list = os.listdir('.')
	for _file in file_list:
		_file_type = subprocess.check_output(['file', _file])
		if "gzip" in str(_file_type):
			os.system("mv {} archives/".format(_file))
		elif "ELF" in str(_file_type):
			os.system("mv {} binaries/".format(_file))
		elif "script" in str(_file_type):
			os.system("mv {} scripts/".format(_file))
		elif "directory" in str(_file_type):
			pass
		elif "script" not in str(_file_type):
			if "ASCII text" in str(_file_type):
				with open(_file, 'r') as _potential_script:
					text = _potential_script.readlines()
				for _line in text:
					if re.search(r'\#\!\/[a-z]+\/[a-z]+\/[a-z]+', _line):
						os.system("mv {} scripts/".format(_file))
						break
					elif re.search(r'\#\!\/[a-z]+\/[a-z]+\/[a-z]+\s+[a-z]+', _line):
						os.system("mv {} scripts/".format(_file))
						break

main()