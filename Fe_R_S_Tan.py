from FiniteStateMachine import FiniteStateMachine
from StateFactory import State
from TransitionFactory import Transition

from SleepState import Sleeping
from AwakeState import Awake

import time

from StateManager import StateManager

import serial

class Fe_R_S_Tan():
    ''' Fe_R_S_Tan Holds all the States, Fe_R_S_Tan for President '''

    def __init__(self):
        self. FiniteStateMachine = FiniteStateMachine(self)
        self.OpenCMPort = None

    def InitStates(self,OpenCMPort,ArduinoPort):
        self.FiniteStateMachine.AddState("Sleeping", Sleeping(self.FiniteStateMachine, OpenCMPort , ArduinoPort))
        self.FiniteStateMachine.AddState("Awake", Awake(self.FiniteStateMachine, ArduinoPort  , OpenCMPort ))
        self.OpenCMPort = OpenCMPort

    def InitTransitions(self):
        self.FiniteStateMachine.AddTransition("toAwake", Transition("Awake"))
        self.FiniteStateMachine.AddTransition("ToSleep", Transition("Sleeping"))

    
    def SetDefaultState(self):
        self.FiniteStateMachine.SetState("Sleeping")

    def Execute(self):
        self.FiniteStateMachine.Execute()

    def DefaultEars(self):
        p = '0'
        tosend = p.encode('utf-8')
        time.sleep(2)
        self.OpenCMPort.write(tosend)
        self.OpenCMPort.flush()
        return True
        

if __name__ == '__main__':
    try:
        opencmport = input("OPEN PORT?")
        OpenCMPort = serial.Serial(opencmport, baudrate=1000000)
        arduinoport = input("Arudino Port?")
        ArduinoPort = serial.Serial(arduinoport, baudrate=1000000)
        print(ArduinoPort)
        

        # OpenCMPort = serial.Serial("/dev/ttyACM0", baudrate=1000000)
        # Raspberry Pi "/dev/ttyACM0"
        # ArduinoPort = serial.Serial("/dev/ttyUSB0", baudrate=1000000)
        # print(OpenCMPort)
        # print(ArduinoPort)
    except:
        exit('! Unable to open OpenCM Port')

    Fe_R_S = Fe_R_S_Tan()
    Fe_R_S.InitStates(OpenCMPort,ArduinoPort)
    Fe_R_S.InitTransitions()
    Fe_R_S.SetDefaultState()
    Fe_R_S.DefaultEars()

   # Manager = StateManager()
   # Manager.setInstance(Fe_R_S)
    

    while True:
        Fe_R_S.Execute()
    
