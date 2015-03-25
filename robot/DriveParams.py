from robot.MotorParams import MotorParams

class DriveParams:

	motorParams=[]
	duration=0 	# number of seconds to dive for
	distance=0	# number of inches to drive for
	obstacleDistance=0	# how far away from obstacles to stop


	def setMotorParams(self, motorIndex, direction, speed):
		print "setMotorParams(" + str(motorIndex) + ")"
		mp = MotorParams(motorIndex, direction, speed)
		found=False
		for index,value in enumerate(self.motorParams):
			if(self.motorParams[index].motorIndex==motorIndex):
				found=True
				self.motorParams[index] = mp
				
		if(not found):
			self.motorParams.append(mp)

	def getMotorParams(self):
		return(self.motorParams);

	def setDuration(self, milliseconds):
		self.duration=int(milliseconds)

	def getDuration(self):
		return(self.duration)

	def setDistance(self, inches):
		self.distance=int(inches)

	def getDistance(self):
		return(self.distance)

	def setObstacleDistance(self, inches):
		self.obstacleDistance=int(inches)

	def getObstacleDistance(self):
		return(self.obstacleDistance)
