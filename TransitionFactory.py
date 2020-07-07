class Transition(object):
	''' Code executed when transitioning from one state to another '''
	def __init__(self, ToState):
		self.ToState = ToState

	def Execute(self):
		print ("Transitioning...")