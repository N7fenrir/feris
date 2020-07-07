
uint32_t period = 1 * 60000L; // for looping for 1 minute

float Velostat[10];
int MinuteVals[30];

int LastSentFeeling;
int CurrentFeeling;

void setup() {
  Serial.begin(1000000);
  pinMode(A1,INPUT_PULLUP);
  digitalWrite(A1, HIGH);
}

void loop() {
 char x = Serial.read();
 if (x == '1'){
  RecordPetting();
  }
}


void (* resetFunc)(void) = 0;


void RecordPetting(){
  int currentMinute = 0;
  for (int TimeLooper = 0 ; TimeLooper < 10 ; TimeLooper ++){
  float average = 0;
  int index = 0;
  for( uint32_t tStart = millis();  (millis()-tStart) < period;  ){
    
    float sensorValue = analogRead(A1);
      MinuteVals[index] = sensorValue;
      Serial.println(sensorValue);
      WriteFeeling(sensorValue);
      index += 1;
    }
    average  = findAverageofArray(MinuteVals, 30);
    Velostat[TimeLooper] = average;
    }
    Terminate(Velostat);
}


float findAverageofArray(int * array, int len){
  float average = 0;
  long sum = 0L;
  for (int index = 0 ; index < len ; index++){
    sum += array[index];
    }
    average = float(sum) / len;
    return average;
 }



void Terminate(float * array){

  WriteChar('W');
  for (int Looper = 0 ; Looper < 10 ; Looper ++) {
    WriteDataBack(array[Looper]);
}
delay(1000);
  WriteChar('T');
  resetFunc();
  }



  
void WriteDataBack(int WriteChar){

  delay(1000);
  Serial.println(WriteChar);
  Serial.flush();
  delay(1000);

}



void WriteFeeling(float WriteChar){

  delay(1000);
  Serial.println(WriteChar);
  Serial.flush();
  delay(1000);

}



 void WriteChar(char Character){
  Serial.println(Character);
  Serial.flush();
  delay(1000);
  }

