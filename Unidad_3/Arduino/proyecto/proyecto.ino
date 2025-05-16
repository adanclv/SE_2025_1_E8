const int nLDR = 4;
int relevadores[3] = {7, 8, 9};
int ldrs[nLDR] = {A0, A1, A2, A3};
int valoresIntens[nLDR];

unsigned long tiempoAnterior = 0;
const unsigned long intervaloLecturas = 100;

void setup() {
  Serial.begin(9600);
  for (int pin = 0; pin < 3; pin++) {
    pinMode(relevadores[pin], OUTPUT);
    digitalWrite(relevadores[pin], LOW);
  }
}

void loop() {
  if (millis()- tiempoAnterior >= intervaloLecturas) {
    tiempoAnterior = millis();
    for (int i = 0; i < nLDR; i++) {
      valoresIntens[i] = analogRead(ldrs[i]);
    }

    Serial.println("I" + String(valoresIntens[0]) + "-" 
                    + String(valoresIntens[1]) + "-" 
                    + String(valoresIntens[2]) + "-" 
                    + String(valoresIntens[3]) + "F");
  }

  if (Serial.available() > 0) {
    int v = Serial.parseInt();
    int estado = digitalRead(relevadores[v]);
    digitalWrite(relevadores[v], !estado);
  }
}
