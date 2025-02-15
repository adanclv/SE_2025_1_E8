int pots[6] = {A0, A1, A2, A3, A4, A5};
int values[6];

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  for (int i = 0; i < 6; i++) {
    values[i] = analogRead(pots[i]);
    delayMicroseconds(1000);
  }

  String c;
  c = "I" + String(values[0]) + "-" + String(values[1]) + "-" + String(values[2]) + "-" + String(values[3]) + "-" + String(values[4]) + "-" + String(values[5]) +"F";
  Serial.println(c);
  delay(100);
}
