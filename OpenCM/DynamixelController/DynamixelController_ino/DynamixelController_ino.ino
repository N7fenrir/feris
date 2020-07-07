#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04

#define R_PanMotor 1
#define R_TiltMotor 2

#define L_PanMotor 3
#define L_TiltMotor 4

#define Tail 6


#define GOAL_SPEED 32
#define CCW_Angle_Limit 8
#define CONTROL_MODE 11

long winkle_1 = 10000;
long winkle_2 = 20000;

long previousMillis = 0;        // will store last time LED was updated
long interval = 10000;           // interval at which to blink (milliseconds)

uint8 aUint8;

Dynamixel Dxl(DXL_BUS_SERIAL1);

void setup() {
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  Dxl.jointMode(L_PanMotor); //jointMode() is to use position mode
  Dxl.jointMode(L_TiltMotor);
  
  Dxl.jointMode(R_PanMotor); //jointMode() is to use position mode
  Dxl.jointMode(R_TiltMotor);
  
  
  
  Sleeping();
}


word Reset_R_L_Pan[6] = 
{
  R_PanMotor, 500, 600,
  L_PanMotor, 500, 600
};


word Reset_R_L_Pan_Slow[6] = 
{
  R_PanMotor, 500, 300,
  L_PanMotor, 500, 300
};

word Set_R_L_Pan[6] = 
{
  R_PanMotor,850,600,
  L_PanMotor,100,600
};

word Set_R_L_Pan_Slow[6] = 
{
  R_PanMotor,850,450,
  L_PanMotor,100,300
};




word Reset_R_L_Tilt[6] = 
{
  
  R_TiltMotor, 100, 600,
  L_TiltMotor, 300,600
};

word Set_R_L_Tilt[6] = 
{
  
  R_TiltMotor, 400, 600,
  L_TiltMotor, 0,600
};


word Set_R_L_Tilt_Slow[6] = 
{
  
  R_TiltMotor, 400, 200,
  L_TiltMotor, 0,200
};

word Set_R_L_Tilt_H[6] = 
{
  
  R_TiltMotor, 200, 600,
  L_TiltMotor, 175,600
};


word Conf_Pan[6] = {
  R_PanMotor,0,600,
  L_PanMotor,1023,600
};


void AckName(){
//  
  Dxl.syncWrite(30,2,Set_R_L_Pan_Slow,6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Tilt_Slow,6);
  delay(100);
  Dxl.syncWrite(30,2,Reset_R_L_Tilt,6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
delay(1000);  
  ResetPositions(); 
}


void debugCheck(){

  Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
  delay(500);
  Dxl.syncWrite(30,2,Reset_R_L_Tilt, 6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Pan,6);
  delay(500);
  Dxl.syncWrite(30,2,Reset_R_L_Pan,6);
  delay(500);
  Dxl.syncWrite(30,2,Reset_R_L_Tilt, 6);
  ResetPositions();



}

void ResetPositions(){
    Dxl.syncWrite(30,2,Reset_R_L_Tilt, 6);
    delay(500);
    Dxl.syncWrite(30,2,Reset_R_L_Pan,6);
}


void Calm(){
  //Move Tail
  int CTime = random(2);  
  for(int Looper = 0 ; Looper < CTime ; Looper++){
   Dxl.writeWord(Tail, GOAL_SPEED, 800);
   Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
   delay(200);
   Dxl.syncWrite(30,2,Set_R_L_Pan,6);
   delay(100);
   Dxl.syncWrite(30,2,Reset_R_L_Tilt,6);
   delay(100);
   Dxl.writeWord(Tail, GOAL_SPEED, 800 | 0x400 );
   Dxl.syncWrite(30,2,Reset_R_L_Pan,6);
   delay(1000);
}
 Dxl.syncWrite(30,2,Set_R_L_Pan,6);
 delay(100);
 Dxl.syncWrite(30,2,Set_R_L_Tilt_H,6);
 delay(500);
 

}


void Annoyed(){
  Dxl.syncWrite(30,2,Set_R_L_Pan,6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Tilt,6);

  int CTime = random(1,9);  
  for(int Looper = 0 ; Looper < CTime ; Looper++){
     Dxl.writeWord(Tail, GOAL_SPEED, 800);
     delay(100);
     Dxl.writeWord(Tail, GOAL_SPEED, 800 | 0x400 );
  }
 
  
}
//
//void Confused(){
//
//  int CTime = random(1,3);
//  if(CTime == 1){
//  Dxl.setPosition(R_TiltMotor,400,800);
//  Dxl.setPosition(R_PanMotor,500,600);
//  Dxl.setPosition(R_PanMotor,850,800);
//  delay(1000);
//  }
//  else{
//  Dxl.setPosition(L_TiltMotor,0,800);
//  Dxl.setPosition(L_PanMotor,500,800);
//  Dxl.setPosition(L_PanMotor,850,800);
//  delay(1000);
//  }
//  Dxl.syncWrite(30,2,Reset_R_L_Tilt,6);
//  delay(500);
//  Dxl.syncWrite(30,2,Conf_Pan,6);
//  delay(500);
// Dxl.syncWrite(30,2,Set_R_L_Tilt_H,6);
//
//}

void Sleep_idle(){
  int CTime = random(1,3);
  if(CTime == 1){
  Dxl.setPosition(R_PanMotor,850,300);
  Dxl.setPosition(R_TiltMotor,200,200);
  delay(1000);
  Dxl.setPosition(R_TiltMotor,400,200);
  Dxl.setPosition(R_PanMotor,500,300);
  }
  else if(CTime == 2){
  Dxl.setPosition(L_PanMotor,100,300);
  Dxl.setPosition(L_TiltMotor,175,200);
  delay(1000);
  Dxl.setPosition(L_TiltMotor,0,200);
  Dxl.setPosition(L_PanMotor, 500,300);
  }
}


void Sleeping(){
  
 Dxl.syncWrite(30,2,Reset_R_L_Pan_Slow,6);

delay(100);
Dxl.syncWrite(30,2,Set_R_L_Tilt_Slow,6);


  
}

void SleepingSlow(){
  
 Dxl.syncWrite(30,2,Reset_R_L_Pan,6);
 delay(100);
 Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
  
}

void loop() {
  
  unsigned long currentMillis = millis();
  
  if(SerialUSB.available() > 0 ){
  WakeUp();
  }
  else if(!SerialUSB.available()){
    if(currentMillis - previousMillis > interval){
      Idling();
      previousMillis = currentMillis;
    }
  }
}


void (* resetFunc)(void) = 0;


void WakeUp(){
  boolean done = false;
  while (done == false){
     aUint8 = SerialUSB.read();
      switch (aUint8){
        case '1':
        AckName();
        SerialUSB.write('C');
        break;    
        case '2':
        Calm();
        break;
        case '3':
        Annoyed();
        break;
        case '5':
        Sleeping();
        break;
        case '9':
        ResetPositions();
        break;
        case '0':
        Sleeping();
        done = true;
        break;
      } 
  }
    
      
}


void Idling(){
  Sleep_idle();
}
