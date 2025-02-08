/*
Practica Unidad 2
*/
int totalLecturas = 30;
int sensor[] = { A0, A1, A2, A3 };

int obtener_Menor(int valor[]) {
  int valorMenor = 1024;
  for (int i = 0; i < totalLecturas; i++) {
    if (valor[i] < valorMenor) {
      valorMenor = valor[i];
    }
  }

  return valorMenor;
}

int obtener_Mayor(int valor[]) {
  int valorMayor = -1;
  for (int i = 0; i < totalLecturas; i++) {
    if (valor[i] > valorMayor) {
      valorMayor = valor[i];
    }
  }

  return valorMayor;
}

int obtener_Mediana(int valor[]) {
  for (int i = 0; i < totalLecturas; i++) { // Bubble Sort
    for (int j = i + 1; j < totalLecturas - 1; j++) {
      if (valor[j] < valor[i]) {
        int temp = valor[i];
        valor[i] = valor[j];
        valor[j] = temp;
      }
    }
  }
  
  return valor[totalLecturas / 2];
}

int obtener_Media(int valor[]) {
  int avg = 0;
  for (int i = 0; i < totalLecturas; i++) {
    avg += valor[i];
  }
  
  avg /= totalLecturas;

  return avg;
}

void setup() {
  Serial.begin(9600);
}

int sensorMedia[30];
int sensorMediana[30];
int sensorMenor[30];
int sensorMayor[30];
void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    sensorMedia[i] = analogRead(sensor[0]);
    sensorMediana[i] = analogRead(sensor[1]);
    sensorMayor[i] = analogRead(sensor[2]);
    sensorMenor[i] = analogRead(sensor[3]);
    delayMicroseconds(100);
  }

  int a = obtener_Media(sensorMedia);
  int b = obtener_Mediana(sensorMediana);
  int c = obtener_Mayor(sensorMayor);
  int d = obtener_Menor(sensorMenor);

  Serial.println(String(a) + ',' + String(b) + ',' + String(c) + ',' + String(d));
  
  delay(10);
}
