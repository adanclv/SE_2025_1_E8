int sensor = A0;
int actuador = 3;
int prev_valor = 0;
int v = 0;
const int totalLecturas = 30;
int valor[30];

unsigned long tiempoAnterior = 0;
const unsigned long intervaloLecturas = 100;

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
  pinMode(actuador, OUTPUT);
}


void loop() {
  if (millis() - tiempoAnterior >= intervaloLecturas) {
    tiempoAnterior = millis();

    for (int i = 0; i < totalLecturas; i++) {
      valor[i] = analogRead(sensor);
      delayMicroseconds(10);
    }

    ordenar_arreglo();
    Serial.println(valor[totalLecturas / 2]);

    if (prev_valor != v) {
      if (prev_valor < v) {
        prev_valor++;
      } else {
        prev_valor--;
      }
      analogWrite(actuador, prev_valor);
    }
  }

  if (Serial.available() > 0) {
    v = Serial.read();
  }
}