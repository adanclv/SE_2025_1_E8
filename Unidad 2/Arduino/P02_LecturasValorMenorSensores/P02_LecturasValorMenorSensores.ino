/*
  Valor Menor
*/
int sensor = A0;
void setup() {
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30];
int valorMenor = 1024; // Valor mas grande porque el valor maximo de lectura de un sensor es 1023
void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }
  valorMenor = 1024;
  for (int i = 0; i < totalLecturas; i++) {
    if (valor[i] < valorMenor) {
      valorMenor = valor[i];
    }
  }
  
  Serial.println(valorMenor);
  delay(10);
}
