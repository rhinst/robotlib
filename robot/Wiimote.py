import cwiid
import time
from util.Observer import Observable

class Wiimote(Observable):

	wm = None
	handlers = {}
	currDir = 0

	def __init__(self):
		Observable.__init__(self);

	def connect(self):
		print 'Press 1+2 on your Wiimote now...'
		self.wm = None
		i=2
		while not self.wm:
			try:
				self.wm=cwiid.Wiimote()
			except RuntimeError:
				if (i>5):
					print("cannot create connection")
					quit()
				print "Error opening wiimote connection"
				print "attempt " + str(i)
				i +=1
		
		#set wiimote to report button presses and accelerometer state
		self.wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
	
		#turn on led to show connected
		self.wm.led = 1


	def processEvents(self):
		driving=False
		buttons = self.wm.state['buttons']
	
		if(buttons & cwiid.BTN_UP):
			self.notifyObservers({'btn':'dpad_up'})
			self.currDir=cwiid.BTN_UP
		elif(buttons & cwiid.BTN_DOWN):
			self.notifyObservers({'btn':'dpad_down'})
			self.currDir=cwiid.BTN_DOWN
		elif(buttons & cwiid.BTN_RIGHT):
			self.notifyObservers({'btn':'dpad_right'})
			self.currDir=cwiid.BTN_RIGHT
		elif(buttons & cwiid.BTN_LEFT):
			self.notifyObservers({'btn':'dpad_left'})
			self.currDir=cwiid.BTN_LEFT
		elif(self.currDir > 0):
			self.notifyObservers({'btn':'dpad_release'})
			self.currDir=0

		if(buttons & cwiid.BTN_1):
			self.notifyObservers({'btn':'btn_1'})
		if(buttons & cwiid.BTN_2):
			self.notifyObservers({'btn':'btn_2'})
		if(buttons & cwiid.BTN_A):
			self.notifyObservers({'btn':'btn_a'})
		if(buttons & cwiid.BTN_B):
			self.notifyObservers({'btn':'btn_b'})
		if(buttons & cwiid.BTN_MINUS):
			self.notifyObservers({'btn':'btn_minus'})
		if(buttons & cwiid.BTN_PLUS):
			self.notifyObservers({'btn':'btn_plus'})
