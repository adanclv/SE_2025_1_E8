//para decision
int leds[3] = {9, 10, 11};

//para ultrasonico - distancia
int Pin_echo = 13;
int Pin_trig = 12;

//para velocidad
int potTemp = A0;

void setup() {
  Serial.begin (9600);
  Serial.setTimeout(10);

  //Ultrasonico
  pinMode(Pin_trig, OUTPUT);
  pinMode(Pin_echo, INPUT);

  for(int i = 0; i<3; i++){
    pinMode(leds[i], OUTPUT);
  }
}

 int pulso, cm;
 int  decision;
 int valor;
void loop() {
  digitalWrite(Pin_trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Pin_trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Pin_trig, LOW);

  pulso = pulseIn(Pin_echo, HIGH); //Medición del ancho de pulso recibido en el pin Echo
  cm = pulso / 29 / 2;             // Convertimos ese pulso en una distancia y a cm

  Serial.println("D" + String(cm));

  valor = analogRead(potTemp);
  Serial.println("V" + String(valor));

  if(Serial.available()>0){
    decision = Serial.readString().toInt();
    if (decision>10){
      decision = decision%10;
    }
    Serial.println(decision);
    for(int i = 0; i<3; i++){
      digitalWrite(leds[i], LOW);
  }
    digitalWrite(leds[decision], HIGH);
  }

  delay(100);
}