import sys
import time
import smbus
from threading import Timer
from robot import MotorParams


REMOTE_DEVICE_ADDRESS = 0x26
DEVICE_REG_MODE1 = 0x00

ACTION_STOP_MOTORS = 1
ACTION_DRIVE_MOTORS = 2

MOTOR_FL = 128
MOTOR_FR = 64
MOTOR_RL = 32
MOTOR_RR = 16
MOTOR_ALL = 240

DIR_BACKWARD_FL = 8
DIR_BACKWARD_FR = 4
DIR_BACKWARD_RL = 2
DIR_BACKWARD_RR = 1
DIR_BACKWARD_ALL = 15

DIR_FORWARD_FL = 0
DIR_FORWARD_FR = 0
DIR_FORWARD_RL = 0
DIR_FORWARD_RR = 0
DIR_FORWARD_ALL = 0

SPEED_NONE_FL = 0
SPEED_ONETHIRD_FL = 64
SPEED_TWOTHIRDS_FL = 128
SPEED_FULL_FL = 192

SPEED_NONE_FR = 0
SPEED_ONETHIRD_FR = 16
SPEED_TWOTHIRDS_FR = 32
SPEED_FULL_FR = 48

SPEED_NONE_RL = 0
SPEED_ONETHIRD_RL = 4
SPEED_TWOTHIRDS_RL = 8
SPEED_FULL_RL = 12

SPEED_NONE_RR = 0
SPEED_ONETHIRD_RR = 1
SPEED_TWOTHIRDS_RR = 2
SPEED_FULL_RR = 3

SPEED_NONE_ALL = 0
SPEED_ONETHIRD_ALL = 85
SPEED_TWOTHIRDS_ALL = 170
SPEED_FULL_ALL = 255

class Motors:
	
	bus = None
	driving=False

	def __init__(self):
		self.bus = smbus.SMBus(1)

	def _write_bus(self, action, args):
		retry=0
		while(retry<3):
			#smbus IO errors are common. try up to 3 times
			try:
				self.bus.write_i2c_block_data(REMOTE_DEVICE_ADDRESS, action, args)
				time.sleep(0.01)
			except IOError:
				# wait and try again
				print "I2C bus error. Retrying..."
				retry += 1
				time.sleep(0.05)
			else:
				#success. break the loop
				retry=3

	def drive(self, driveParams):
		#TODO: combine motorparams objects with identical speeds/dirs into a single bus write
		for mp in driveParams.getMotorParams():
			self._write_bus(ACTION_DRIVE_MOTORS, [mp.motorIndex + (mp.direction*(mp.motorIndex/16)), (mp.motorIndex*mp.motorIndex/256)])

		#check for stop conditions
		if(driveParams.getDuration() > 0):
			t = Timer(driveParams.getDuration()/1000, self.stopAll)
			t.start()
				
			

	def driveForward(self):
		self.driving=True
		self._write_bus(ACTION_DRIVE_MOTORS, [MOTOR_ALL + DIR_FORWARD_ALL, SPEED_FULL_ALL])

	def driveBackward(self):
		self.driving=True
		self._write_bus(ACTION_DRIVE_MOTORS, [MOTOR_ALL + DIR_BACKWARD_ALL, SPEED_FULL_ALL])

	def turnLeft(self):
		self.driving=True
		self._write_bus(ACTION_DRIVE_MOTORS, [MOTOR_FR + MOTOR_RR + DIR_FORWARD_ALL, SPEED_FULL_ALL])
		self._write_bus(ACTION_DRIVE_MOTORS, [MOTOR_FL + MOTOR_RL + DIR_BACKWARD_ALL, SPEED_FULL_ALL])


	def turnRight(self):
		self.driving=True
		self._write_bus(ACTION_DRIVE_MOTORS, [MOTOR_FL + MOTOR_RL + DIR_FORWARD_ALL, SPEED_FULL_ALL])
		self._write_bus(ACTION_DRIVE_MOTORS, [MOTOR_FR + MOTOR_RR + DIR_BACKWARD_ALL, SPEED_FULL_ALL])

	def stopAll(self):
		print "Stopping motors"
		self.driving=False
		self._write_bus(ACTION_STOP_MOTORS, [240])
