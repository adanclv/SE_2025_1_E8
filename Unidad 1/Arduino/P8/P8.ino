// P8
int sensor = A0;
int actuador = 6;

void setup() {
	Serial.begin(9600);
}

int v;
void loop() {
	v = analogRead(sensor);
	v = v / 4;
	analogWrite(actuador, v);
	delay(100);
}