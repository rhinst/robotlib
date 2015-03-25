import sys
import time
import threading
from robot.EventHandler import EventHandler
from robot.Wiimote import Wiimote
from robot.Server import RobotServer
from robot.Motors import Motors

class Robot:

	config = None
	eh = None
	server = None
	motors = None

	def __init__(self, config):
		self.config = config
		self.eh = EventHandler(config, self)
		self.initMotors()
		self.initServer()


	def initServer(self):
		self.server = RobotServer(1, 'server-thread', self.config)
		self.server.addObserver(self.eh)
		self.server.daemon=True
		self.server.start()

	def initMotors(self):
		self.motors = Motors()		
	

	def start(self):
		while(True):
			#remote.processEvents()
			time.sleep(0.1)


	def shutdown(self):
		self.server.shutdown()
		sys.exit(0)
