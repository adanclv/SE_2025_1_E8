const int totalLecturas = 30;
int sensor[] = { A0, A1, A2, A3, A4, A5 };

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

int obtener_Moda(int valor[]) {
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
      auxiliarCount = 1;
    } else {
      auxiliarCount++;
    }

    if (auxiliarCount > contador) {
      contador = auxiliarCount;
      moda = valor[i];
    }
  }
  return moda;
}

void setup() {
  Serial.begin(9600);
}

int sensorMedia[30];
int sensorMediana[30];
int sensorMenor[30];
int sensorMayor[30];
int sensorModa[30];
int base[30];
void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    sensorMedia[i] = analogRead(sensor[0]);
    sensorMediana[i] = analogRead(sensor[1]);
    sensorMayor[i] = analogRead(sensor[2]);
    sensorMenor[i] = analogRead(sensor[3]);
    sensorModa[i] = analogRead(sensor[4]);
    base[i] = analogRead(sensor[5]);
    delayMicroseconds(100);
  }

  int a = obtener_Media(sensorMedia);
  int b = obtener_Mediana(sensorMediana);
  int c = obtener_Mayor(sensorMayor);
  int d = obtener_Menor(sensorMenor);
  int e = obtener_Moda(sensorModa);
  int f = base[29];

  Serial.println(String(a) + ',' + String(b) + ',' + String(c) + ',' + String(d) + ',' + String(e) + ',' + String(f));
  
  delay(100);
}