from FiniteStateMachine import FiniteStateMachine
from StateFactory import State
from TransitionFactory import Transition

from SleepState import Sleeping
from AwakeState import Awake
from Annoyed import Annoyed
from CalmState import Calm

import datetime
import time


class StateManager():

    def __init__(self):
        self.currentState = "Sleeping"
        self.EndTime = None
        self.StartTime = None
        self.StateTransitions = []

    def setInstance(self, Cat):
        self.Monitor = Cat
    
    def RecordObservations(self):
        currentState = self.Monitor.FiniteStateMachine.getCurrentState()
        self.StateTransitions.append(currentState)
        if(currentState == "Awake"):
            tempDate = datetime.datetime.now()
            self.startTime = (tempDate.hour , tempDate.minute)
            self.EndTime = time.time() + 60 * 10
            
        else:
            pass