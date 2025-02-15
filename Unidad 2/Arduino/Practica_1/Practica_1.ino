/*
Práctica 1 Unidad 2
*/
const int totalLecturas = 30;
int sensor[] = { A0, A1, A2, A3, A4, A5 };
int aux = -1;

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

int valores[6][totalLecturas];
int media[6];
int mediana[6];
int mayor[6];
int menor[6];
int moda[6];
int base[6];
void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    valores[0][i] = analogRead(sensor[0]);
    valores[1][i] = analogRead(sensor[1]);
    valores[2][i] = analogRead(sensor[2]);
    valores[3][i] = analogRead(sensor[3]);
    valores[4][i] = analogRead(sensor[4]);
    valores[5][i] = analogRead(sensor[5]);
    delayMicroseconds(100);
  }

  for (int i = 0; i < 6; i++) {
    media[i] = obtener_Media(valores[i]);
    mediana[i] = obtener_Mediana(valores[i]);
    mayor[i] = obtener_Mayor(valores[i]);
    menor[i] = obtener_Menor(valores[i]);
    moda[i] = obtener_Moda(valores[i]);
    base[i] = valores[i][totalLecturas-1];
  }

    Serial.println(
        String(media[0]) + "," + String(media[1]) + "," + String(media[2]) + "," + String(media[3]) + "," + String(media[4]) + "," + String(media[5]) + ";" +
        String(mediana[0]) + "," + String(mediana[1]) + "," + String(mediana[2]) + "," + String(mediana[3]) + "," + String(mediana[4]) + "," + String(mediana[5]) + ";" +
        String(mayor[0]) + "," + String(mayor[1]) + "," + String(mayor[2]) + "," + String(mayor[3]) + "," + String(mayor[4]) + "," + String(mayor[5]) + ";" +
        String(menor[0]) + "," + String(menor[1]) + "," + String(menor[2]) + "," + String(menor[3]) + "," + String(menor[4]) + "," + String(menor[5]) + ";" +
        String(moda[0]) + "," + String(moda[1]) + "," + String(moda[2]) + "," + String(moda[3]) + "," + String(moda[4]) + "," + String(moda[5]) + ";" +
        String(base[0]) + "," + String(base[1]) + "," + String(base[2]) + "," + String(base[3]) + "," + String(base[4]) + "," + String(base[5])
    );
  delay(100);
}