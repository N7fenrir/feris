import sys
import os
import time
import pyaudio
import threading


from FiniteStateMachine import FiniteStateMachine
from StateFactory import State

from pocketsphinx import LiveSpeech

class Sleeping(State):
    ''' Sleep State :  A State where Cat can recieve the name
        and the touch input to go to AWAKE State '''

    def __init__(self, FiniteStateMachine, OpenCM , Arduino):
        self.OpenCMPort = OpenCM
        self.ArduinoPort = Arduino
        self.NameRecognized = False
        super(Sleeping, self).__init__(FiniteStateMachine)
        
    def OnStateStart(self):
        print("Entered the State Sleeping")
        self.NameRecognized = False
        super(Sleeping, self).OnStateStart()

    def Execute(self):
        print("Listening to Name")
        if self.NameRecognized == False:
            self.NameRecognized = self.NameRecognition("ferris")
            if self.NameRecognized == True:
                bufferCheck = self.MoveEars()
                self.FiniteStateMachine.TransitionTo("toAwake")



    def Exit(self):
        print("Exiting Sleep State and going to State Wake")   

    def NameRecognition(self,ListenToName):
        speech = LiveSpeech(lm=False, keyphrase=ListenToName, kws_threshold=1e-40)
        for phrase in speech:
            if (str(phrase) == str(ListenToName)):
                self.NameRecognized = True
                return True


    def MoveEars(self):
        p = '1'
        data = None
        tosend = p.encode('utf-8')
        time.sleep(2)
        self.OpenCMPort.write(tosend)
        self.OpenCMPort.flush()
        data  = self.OpenCMPort.read()
        data = str(data,"utf-8")
        if (data!=None):
            print(data)
            return True
        
        
'''     def NameRecognition(self, ListenToName):
        modelDir = "files/Sphinx/models"

        config = pocketsphinx.Decoder.default_config()
        config.set_string("-hmm", os.path.join(modelDir, "en-us/en-us-ptm"))
        config.set_string('-dict', os.path.join(modelDir, 'en-us/cmudict-en-us.dict'))
        config.set_string('-keyphrase', ListenToName)
        config.set_string('-logfn', 'files/sphinx.log')
        config.set_float('-kws_threshold', 1e-20)
        
        pyaud = pyaudio.PyAudio()
        stream =  pyaud.open(format=pyaudio.paInt16, channels=1, rate=48000, input=True, input_device_index = 2, frames_per_buffer=512)
        stream.start_stream()
        
        
        decoder = pocketsphinx.Decoder(config)
        decoder.start_utt()

        while True:
            buffer = stream.read(512)

            if buffer:
                decoder.process_raw(buffer, False, False)
            else:
                break
            
            if decoder.hyp() is not None:
                decoder.end_utt()
                decoder.start_utt()
                return True  '''
''' 
    def PythonMicTest(self, s):
        po = pyaudio.PyAudio()
        for index in range(po.get_device_count()):
            desc = po.get_device_info_by_index(index)
            print("DEVICE: %s  INDEX:  %s  RATE:  %s " %  (desc["name"], index,  int(desc["defaultSampleRate"])))

        return True


 '''




