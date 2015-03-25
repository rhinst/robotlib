import os
import sys
import io
from ConfigParser import RawConfigParser


class Config(RawConfigParser):
	
	def __init__(self, filename):
		if(os.path.exists(filename)):
			with open(filename) as f:
				content = f.read()

			RawConfigParser.__init__(self, allow_no_value=True)
			self.readfp(io.BytesIO(content))
		else:
			print "File not found: " + filename
			sys.exit()


	@staticmethod
	def getDefaultConfigFile():
		return(os.environ['HOME'] + '/.robot/config.ini')
