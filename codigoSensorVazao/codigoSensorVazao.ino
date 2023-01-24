double calculoVazao;
volatile int contador;
long int timeStemp = millis();

#import <SoftwareSerial.h>
SoftwareSerial mySerial{8,9};

void setup() {
  pinMode(2,INPUT); // Configura o pino 2 como entrada de dados
  attachInterrupt(0,Vazao,RISING); // Quando a turbina do sensor girar, irá chamar o método vazão
  Serial.begin(9600); // Configura o baudrate para 9600
  mySerial.begin(9600);
}

void loop() {
 
  contador = 0; 
  interrupts();
  delay(1000);
  noInterrupts();

  if ((millis() - timeStemp) < 5000){
    timeStemp = millis();
    calculoVazao = (contador*2.25); // vazão registrada em ml
    mySerial.println(calculoVazao);
  }
}

void Vazao(){
  contador++;
}
