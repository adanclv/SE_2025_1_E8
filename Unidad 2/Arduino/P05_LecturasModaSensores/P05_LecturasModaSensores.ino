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

  for (int i = 0; i < totalLecturas; i++) {
    for (int j = i + 1; j < totalLecturas - 1; j++) {
      int temp = valor[i];
      valor[i] = valor[j];
      valor[j] = temp;
    }
  }
  
  int contador = 1;
  int moda = valor[0];
  int auxiliarCount = 1;
  for (int i = 0; i < totalLecturas - 1; i++) {
    if (valor[i] != valor[i+1]) {
      auxiliaCount = 1;
    } else {
      auxiliarCount++;
    }

    if (auxiliarCount > contador) {
      contador = auxiliarCount;
      moda = valor[i];
    }
  }
  
  delay(10);
}