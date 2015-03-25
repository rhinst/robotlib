MOTOR_FL = 128
MOTOR_FR = 64
MOTOR_RL = 32
MOTOR_RR = 16

DIR_FORWARD=0
DIR_BACKWARD=1

SPEED_NONE=0
SPEED_ONE_THIRD=1
SPEED_TWO_THIRDS=2
SPEED_FULL=3

class MotorParams:

	motorIndex=MOTOR_FL
	direction=DIR_FORWARD
	speed=SPEED_FULL

	def __init__(self, motorIndex, direction, speed):
		self.motorIndex=int(motorIndex)
		self.direction=int(direction)
		self.speed=int(speed)
