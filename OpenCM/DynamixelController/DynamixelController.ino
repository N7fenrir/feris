
#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04


// Right Ear Motors
#define R_Pan 1
#define R_Tilt 2

// Left Ear Motors
#define L_Pan 3
#define L_Tilt 4

// Tail Motor
#define Tail_Motor 6


Dynamixel Dxl(DXL_BUS_SERIAL1);

int counter;
bool onlyOnceHappened;

// aUint8 byte to recieve messages from the Pi/PC
uint8 aUint8;


void blinkOnce()
{
  digitalWrite(BOARD_LED_PIN, LOW);
  delay_us(100);
  digitalWrite(BOARD_LED_PIN, HIGH);
}


void setup() {
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  Dxl.jointMode(L_Pan); //jointMode() is to use position mode
  Dxl.jointMode(L_Tilt);
  
  Dxl.jointMode(R_Pan); //jointMode() is to use position mode
  Dxl.jointMode(R_Tilt);
  
  pinMode(BOARD_LED_PIN, OUTPUT);
  onlyOnceHappened=false;
  counter=0;
}

word Reset_R_L_Pan[6] = 
{
  R_PanMotor, 500, 600,
  L_PanMotor, 500, 600
};

word Set_R_L_Pan[6] = 
{
  R_PanMotor,850,600,
  L_PanMotor,100,600
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



void ResetPosition(){
  Dxl.syncWrite(30,2,Reset_R_L_Tilt, 6);
  delay(500);
  Dxl.syncWrite(30,2,Reset_R_L_Pan, 6);
  delay(500);
}


void AckName(){
  Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
  delay(500);
  Dxl.syncWrite(30,2,R_L_Tilt_Reset, 6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Tilt,6);
  delay(500);
  Dxl.syncWrite(30,2,Set_R_L_Pan,6);
  delay(500);
  Dxl.syncWrite(30,2,R_L_Tilt_Reset, 6);
}


void loop() 
{    
  if (SerialUSB.available())
  {
    aUint8 = SerialUSB.read() - '0'; 
    int checkVal = int (aUint8);   
    switch (aUint8){
      case '1':
        //Ack Name, Move Ears and Tail
        AckName();
        delay(1000);
        break;
      case '2':
         //somefunction
        break;
      case '3':
        //some function
        break;
      case '4':
        //some function
        break;
      case '5':
        //some function
        break; 
      case '6':
        //some function
        break;
      case '7':
        //some function
        break;
      case '8':
        //some function
        break;
      case '9':
        //some function
        break;   
    }
    SerialUSB.write(aUint8);
  } 
  
}







