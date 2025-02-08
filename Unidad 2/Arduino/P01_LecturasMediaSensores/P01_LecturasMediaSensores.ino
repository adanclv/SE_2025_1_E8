/*
  - Preprocesamiento de datos -
  Normalmente leemos unicamente una vez cada sensor y mandamos la información al puerto serial.
  Esto es incorrecto debido a que podrian generarse inconsistencias en las lecturas, por lo que 
  debe buscarse y tratar de aminorar esta situación mediante el preprocesamiento.
*/
int sensor = A0;
void setup() {
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30];
void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  int avg = 0;
  for (int i = 0; i < totalLecturas; i++) {
    avg += valor[i];
  }
  
  avg /= totalLecturas;

  Serial.println(avg);

  delay(10);
}
