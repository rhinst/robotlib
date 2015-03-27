import smbus
import time
from robot.Adafruit_PWM_Servo_Driver import PWM

REMOTE_DEVICE_ADDRESS = 0x40
DEVICE_REG_MODE1 = 0x00


class Servos:

	config = None
	pwm = None
	servoMins = [200,300]
	servoMaxs = [540,550]
	servoCenters = [390,390]

	def __init__(self, config):
		self.pwm = PWM(0x40)
		self.config = config

	def reset(self):
		for n in range(2):
  			self.pwm.setPWM(n, 0, self.servoCenters[n])
  			self.pwm.setPWM(n, 0, self.servoCenters[n])

	def test(self):
		self.pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
		for i in range(5):
  			# Change speed of continuous servo on channel O
			for n in range(2):
  				self.pwm.setPWM(n, 0, self.servoMins[n])
  				time.sleep(1)
  				self.pwm.setPWM(n, 0, self.servoMaxs[n])
  				time.sleep(1)

	def lookAround(self):
		#look left
  		self.pwm.setPWM(0, 0, 200)
		time.sleep(0.05)

		#look up
  		self.pwm.setPWM(1, 0, 300)
		time.sleep(0.05)

		for n in range(20):
			self.pwm.setPWM(0, 0, int(200+(n*17)))
			time.sleep(0.05)

		#look middle
  		self.pwm.setPWM(1, 0, 425)
		time.sleep(0.05)

		for n in range(20):
			self.pwm.setPWM(0, 0, int(200+((20-n)*17)))
			time.sleep(0.05)

		#look down
  		self.pwm.setPWM(1, 0, 550)
		time.sleep(0.05)

		for n in range(20):
			self.pwm.setPWM(0, 0, int(200+(n*17)))
			time.sleep(0.05)
