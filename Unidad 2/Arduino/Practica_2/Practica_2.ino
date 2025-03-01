int sensor = A0;
const int totalLecturas = 30;
int valor[30];

void ordenar_arreglo() { // Bubble sort
  for (int i = 0; i < totalLecturas - 1; i++) {  
    for (int j = 0; j < totalLecturas - 1 - i; j++) {
      if (valor[j] > valor[j + 1]) {
        int temp = valor[j];
        valor[j] = valor[j + 1];
        valor[j + 1] = temp;
      }
    }
  }
}

void setup() {
  Serial.begin(9600);
}

void loop() {
    for (int i = 0; i < totalLecturas; i++) {
      valor[i] = analogRead(sensor);
      delayMicroseconds(100);
    }

    ordenar_arreglo();

    Serial.println(valor[totalLecturas / 2]);

    delay(1000);
}