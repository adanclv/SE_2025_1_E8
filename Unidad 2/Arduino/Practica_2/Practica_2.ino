int sensor = A0;
int pin[] = {8, 9, 10};

unsigned long tiempoAnterior = 0;
const unsigned long intervaloLecturas = 100;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 3; i++) {
    pinMode(pin[i], OUTPUT);
  }
}

int totalLecturas = 30;
int valor[30];
void loop() {
  if (millis() - tiempoAnterior >= intervaloLecturas) {
    tiempoAnterior = millis();

    for (int i = 0; i < totalLecturas; i++) {
      valor[i] = analogRead(sensor);
      delayMicroseconds(100);
    }

    for (int i = 0; i < totalLecturas - 1; i++) {  
      for (int j = 0; j < totalLecturas - 1 - i; j++) {
        if (valor[j] > valor[j + 1]) {
          int temp = valor[j];
          valor[j] = valor[j + 1];
          valor[j + 1] = temp;
        }
      }
    }

    Serial.println(valor[totalLecturas / 2]);
  }

  if (Serial.available() > 0) {
    int v = Serial.readString().toInt();
    for (int i = 0; i < 3; i++) {
      digitalWrite(pin[i], LOW);
    }
    for (int i = 0; i < v; i++) {
        digitalWrite(pin[i], HIGH);
    }
  }
}