



from StateFactory import State
from FiniteStateMachine import FiniteStateMachine


class Annoyed(State):
    ''' The Cat is now in Annoyed State '''

    def __init__(self, FiniteStateMachine, OpenCM , Arduino):
        self.ArduinoPort = Arduino
        self.OpenCMPort = OpenCM
        super(Annoyed, self).__init__(FiniteStateMachine)
    
    def OnStateStart(self):
        print("Cat is now in Annoyed State")
    
    def Execute(self):
        print("Executing State specific Functions")

    def Exit(self):
        print("Cat no longer in annoyed State")
