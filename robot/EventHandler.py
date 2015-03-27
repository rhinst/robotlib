import re
from robot.Observer import Observer
from robot.DriveParams import DriveParams
from robot import MotorParams


class EventHandler(Observer):

	config = None
	robot = None

	def __init__(self, config, robot):
		self.config = config
		self.robot = robot

	def update(self, observable, params):
		if(observable.__class__.__name__=='RobotServer'):
			cmd = params['cmd']
			args = params['args']
			print "Received command from server: " + cmd
			if(cmd == 'shutdown'):
    				command = "/usr/bin/sudo /sbin/shutdown -h now"
    				import subprocess
    				process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    				output = process.communicate()[0]
    				print output
			if(cmd == 'drive'):
				dp = DriveParams()
				motorIds = {'fl':MotorParams.MOTOR_FL,'fr':MotorParams.MOTOR_FR,'rl':MotorParams.MOTOR_RL,'rr':MotorParams.MOTOR_RR}
				for m in motorIds.keys():
					motorId=motorIds[m]
					key = m + '_speed'
					if key not in args:
						speed=0
					else:
						speed=args[key]
					key = m + '_dir'
					if key not in args:
						dir=0
					else:
						dir=args[key]

					dp.setMotorParams(motorId, dir, speed)

				if('duration' in args):
					dp.setDuration(args['duration'])

				if('distance' in args):
					dp.setDistance(args['distance'])

				if('obstacle' in args):
					dp.setObstacleDistance(args['obstacle'])

				#start the motors
				self.robot.motors.drive(dp)
