
from random import randint
import time
import random

from TransitionFactory import Transition

class FiniteStateMachine(object):
    ''' Finite State Mahcine Base Model '''
    def __init__(self, character):
        self.char = character
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.previousState = None
        self.transitionTo = None


    def AddTransition(self, TransitionName, transition):
        self.transitions[TransitionName] = transition

    def AddState(self, stateName, state):
        self.states[stateName] = state


    def SetState(self, stateName):
        self.previousState = self.currentState
        self.currentState = self.states[stateName]
    
    def TransitionTo(self, Transition_to_State):
        self.transitionTo = self.transitions[Transition_to_State]


    def Execute(self):
        if (self.transitionTo):
            self.currentState.Exit()
            self.transitionTo.Execute()
            self.SetState(self.transitionTo.ToState)
            self.currentState.OnStateStart()
            self.transitionTo = None 
        self.currentState.Execute()


    def GetCurrentState(self):
        return str(type(self.currentState).__name__)
    
    def SendCurrentState(self):
        return str(type(self.currentState).__name__)




