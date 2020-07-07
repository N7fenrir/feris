


from StateFactory import State
from FiniteStateMachine import FiniteStateMachine


class Calm(State):
    ''' State where the Cat is calm '''

    def __init__(self, FiniteStateMachine, OpenCM , Arduino):
        self.OpenCMPort = OpenCM
        self.Arduino = Arduino
        super(Calm, self).__init__(FiniteStateMachine)
    
    def OnStateStart(self):
        print("State Calm has Started")
    
    def Execute(self):
        print("Executing State Based Functions")

    def Exit(self):
        print("Cat has exited the Calm Sate")