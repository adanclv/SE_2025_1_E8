/*
  Mediana
*/
int sensor[] = { A0, A1, A2, A3 };
void setup() {
  Serial.begin(9600);
}

int totalLecturas = 30;p
int valor[30];
void loop() {
  for (int i = 0; i < totalLecturas; i++) {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  for (int i = 0; i < totalLecturas; i++) { // Bubble Sort
    for (int j = i + 1; j < totalLecturas - 1; j++) {
      if (valor[j] < valor[i]) {
        int temp = valor[i];
        valor[i] = valor[j];
        valor[j] = temp;
      }
    }
  }
  
  Serial.println(valor[totalLecturas / 2]);
  delay(10);
}
