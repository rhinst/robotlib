from SocketServer import TCPServer,StreamRequestHandler
from robot.Observer import Observable
from threading import Thread

class RobotServer(TCPServer,Observable, Thread):

	def __init__(self, threadID, name, config):
		TCPServer.__init__(self, (config.get('server','address'), config.getint('server', 'port')), RobotTCPHandler)
		Observable.__init__(self)
		Thread.__init__(self)
		self.threadID=threadID
		self.name=name

	def run(self):
		self.serve_forever()

	def shutdown(self):
		TCPServer.shutdown()


class RobotTCPHandler(StreamRequestHandler):
	

	def handle(self):
        	data = self.rfile.readline().strip()
		parts = data.split(' ')

		cmd = parts[0]
		params = {}
		for arg in parts[1:]:
			keyval = arg.split('=')
			params[keyval[0]] = keyval[1]


		self.server.setChanged()
		self.server.notifyObservers({'cmd': cmd, 'args': params})

        	self.wfile.write("OK")
