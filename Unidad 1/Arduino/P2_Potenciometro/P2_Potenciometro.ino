int sensores[] = {A0, A1, A2, A3};
int actuadores[] = {8, 9, 10, 11};
int i;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  for (i = 0; i < 4; i++) {
    pinMode(actuadores[i], OUTPUT);
  }
} 

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  for (i = 0; i < 4; i++) {
    valor = analogRead(sensores[i]);
    valor = int(valor / 512);
    digitalWrite(actuadores[i], valor);
  }
}
