// P5
int pinPWM = 6;

void setup() {
	Serial.begin(9600);
}

void loop() {
	for(int i = 0; i < 255; i++) {
		analogWrite(pinPWM, i);
		delayMicroseconds(10);
	}
	delay(100);
	for (int i = 255; i > 0; i--) {
		analogWrite(pinPWM, i);
		delayMicroseconds(10);
	}
	delay(10);
}