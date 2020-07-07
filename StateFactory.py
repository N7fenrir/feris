


class State(object):
    ''' Base Template of the State which all other Get methods from'''
    def __init__(self, FiniteStateMachine):
        self.FiniteStateMachine = FiniteStateMachine

    def OnStateStart(self):
        pass    
    
    def Execute(self):
        pass
    
    def Exit(self):
        pass

        