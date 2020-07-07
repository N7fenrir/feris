import sys
import os
import datetime
import time
import json
import serial
import pyaudio
import numpy

from StateFactory import State
from FiniteStateMachine import FiniteStateMachine

from pocketsphinx import LiveSpeech





class Awake(State):
    ''' Awake State : - Here In This State the Cat is Awake and Reacts'''

    def __init__(self, FiniteStateMachine, Arduino, OpenCm):
        self.ArduinoPort = Arduino
        self.OpenCMPort = OpenCm
        self.NamceAck = False
        self.NameRecvdAgain = None
        self.RecordPetting = []
        self.recvdSignal = None
        super(Awake, self).__init__(FiniteStateMachine)
        self.filename = "data/data.json"



    def OnStateStart(self):
        super(Awake, self).OnStateStart()


    def Execute(self):
       GotoSleep = self.PettingInput()
       if GotoSleep == True:
           self.NamceAck = False
           self.SetToSleep()
           self.FiniteStateMachine.TransitionTo("ToSleep")


    def Exit(self):
        print("Cat is now no longer Awake")


    def PettingInput(self):
        p = "1"
        toSend = p.encode('utf-8')
        time.sleep(2)
        self.ArduinoPort.write(toSend)
        self.ArduinoPort.flush()
        LastFeeling = None
        CurrentFeeling  = None

        Calm_threshold = 850.0
        Annoyed_threshold = 700.0
        Neutral_Treshold = 900.0

        toClose = False
        ExpectedLabels = self.ReadExpectation()
        TimeSpentinCurrent = None

        while  toClose == False:
            Feeling =  (self.ArduinoPort.readline()).rstrip()
            try:
                Feeling = float(Feeling)
                print(Feeling)
                if(Feeling > Neutral_Treshold):
                    CurrentFeeling = "N"
                    if(CurrentFeeling != LastFeeling):
                        print("Neutral")
                    LastFeeling = "N"
                    self.EarInteract("9")

                if(Calm_threshold > Feeling and Feeling > Annoyed_threshold):
                        CurrentFeeling = "C"
                        if(CurrentFeeling != LastFeeling):
                            print("Calm")
                            self.EarInteract("2")
                        LastFeeling = "C"

                if(Feeling < Annoyed_threshold):
                    CurrentFeeling = "A"
                    if(CurrentFeeling != LastFeeling):
                        print("Annoyed")
                        self.EarInteract("3")
                    LastFeeling = "A"

            except ValueError:
                Feeling = str(Feeling, 'utf-8')
                if(Feeling == 'W'):
                    Terminex = False
                    while Terminex == False:
                        Values =  (self.ArduinoPort.readline()).rstrip()
                        try:
                            Values = float(Values)
                            self.RecordPetting.append(Values)
                        except:
                            Values = str(Values, 'utf-8')
                            if (Values == "T"):
                                print(self.RecordPetting)
                                Terminex = self.AppendObservation(self.RecordPetting)
                                toClose = True
                                Terminex = True
                                #self.EarInteract(6)
                                return True
                       


    def EarInteract(self, feelingindex):
        feelingindex = feelingindex.encode('utf-8')
        time.sleep(2)
        self.OpenCMPort.write(feelingindex)
        self.OpenCMPort.flush()
        return True
    
    def NameRecognition(self,ListenToName):
        speech = LiveSpeech(lm=False, keyphrase=ListenToName, kws_threshold=1e-20)
        for phrase in speech:
            if (str(phrase) == str(ListenToName)):
                return True


    def ReadExpectation(self):
        ExpectedLabels = None
        with open(self.filename) as file:
             dataStore = json.loads(file.read())
             ExpectedLabels = dataStore["ExpectedLabels"]
             file.close()
        return ExpectedLabels

    def CalculateExpectations(self,ObservedValues, ExpectedLabels):
        ''' Calculate the Mean Values of the Matrix Columns and then assign the Label. '''
        
        Calm_threshold = 750.0
        Annoyed_threshold = 600.0
        Neutral_Treshold = 900.0
        
        Matrix_Observed = numpy.zeros(shape=(len(ObservedValues),10))
        for index, element in enumerate(ObservedValues):
            Matrix_Observed[index] = list(map(float, ObservedValues[element]))
            MeanValues = Matrix_Observed.mean(0)
            for index, element in enumerate(ExpectedLabels):
                if (MeanValues[index] < Annoyed_threshold):
                    ExpectedLabels[element] = "A"
                elif(Annoyed_threshold < MeanValues[index] < Calm_threshold):
                    ExpectedLabels[element] = "C"
                elif(MeanValues[index] > Neutral_Treshold):
                    ExpectedLabels[element] = "N"

        return ExpectedLabels

    
    def AppendObservation(self, Observation):
        ObservationToAppend = Observation
        ObjectName = "Observation_"
        ObservedValues = None
        ExpectedLabels = None
        with open(self.filename, "r", encoding="utf-8") as file:
            dataStore = json.loads(file.read())
            ObservedValues = dataStore["ObservedValues"]
            ExpectedLabels  = dataStore["ExpectedLabels"]
            NameObject = ObjectName + str(len(ObservedValues) + 1)
            ObservedValues.update({NameObject: ObservationToAppend})
            file.close()
        
        ExpectedLabels = self.CalculateExpectations(ObservedValues, ExpectedLabels)
        newPythonDict = {"ExpectedLabels":ExpectedLabels , "ObservedValues":ObservedValues }
        self.WriteToFile(newPythonDict)
        return True


    def WriteToFile(self,dataDict):
        ''' Function To Write the Dictionary To a json File based on the FileName. '''
        with open(self.filename, "w", encoding = "utf-8") as file:
            json.dump(dataDict, file)
            file.close()

    def SetToSleep(self):
        p = '0'
        tosend = p.encode('utf-8')
        time.sleep(2)
        self.OpenCMPort.write(tosend)
        self.OpenCMPort.flush()
        return True

