// P1
int sensor = A0;

void setup() {
	Serial.begin(9600);
}

int v;

void loop() {
	v = analogRead(sensor);
	Serial.println(v);
	delay(1000);
}

/*
// P2
int sensor = 10;

void setup() {
	Serial.begin(9600);
	pinMode(sensor, INPUT);
}

int v;
void loop() {
	v = digitalRead(sensor);
	Serial.println(v);
	delay(1000);
}

// P3
int actuador = 12;

void setup() {
	Serial.begin(9600);
	pinMode(actuador, OUTPUT)
}

void loop() {
	digitalWrite(actuador, 1);
	delay(1000);
	digitalWrite(actuador, 0);
	delay(1000);
}

// P4
int actuador = 12;

void setup() {
	Serial.begin(9600);
	pinMode(actuador, OUTPUT);
}

void loop() {
	digitalWrite(actuador, 1);
	delay(1000);
	digitalWrite(actuador, 0);
	delay(1000);
}

// P5
int pinAPWM = 6;

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

// P6
long v;

void setup() {
	Serial.begin(9600);
}

void loop() {
	v = millis();
	Serial.println(v);
	delay(1000);
}

// P7
int sensor = A0;
int actuador = 6;

void setup() {
	Serial.begin(9600);
	} 
int v;
void loop() {
	v = analogRead(sensor);
	v = map(v, 0 , 1023, 0, 255)
	analogWrite(actuador, v);
	delay(100);
}

// P8
int sensor = A0;
int actuador = 6;

void setup() {
	Serial.begin(9600);
}

int v;
void loop() {
	v = digitalRead(sensor);
	v = v / 4;
	analogWrite(actuador, v);
	delay(100);
}

// P9
int actuadores[4] = { 8, 9, 10, 11 };

void setup() {
	Serial.begin(9600);
	for (int i = 0; i < 4; i++) {
		pinMode(actuador[i], OUTPUT);
	}
}

void loop() {
	for (int i = 0; i < 4; i++) {
		digitalWrite(actuadores[i], 1);
		delay(100);
		digitalWrite(actuadores[i], 0);
		delay(100);
	}
	delay(100);
}

// P10
int actuadores[4] = { 8, 9, 10, 11 };

void setup() {
	Serial.begin(9600);
	for (int i = 0; i < 4; i++) {
		pinMode(actuador[i], OUTPUT);
	}
	Serial.setTimeout(10);
}

int v;
void loop() {
	if (Seria.available() > 0) {
		v = Serial.readString().toInt();
		digitalWrite(actuador[v], 1);
		delay(100);
		digitalWrite(actuadores[v], 0);
		delay(100);
	}
}

// P11
int actuador = 10;

void setup() {
	Serial.begin(9600);
	Serial.setTimeout(10);
	pinMode(actuador, OUTPUT);
}

int v;
void loop() {
	if (Serial.available() > 0) {
		v = Serial.readString().toInt();
		digitalWrite(actuador, v);
	}
	delay(100);
}

// P12
int sensor = A0;
e
void setup() {
	Serial.begin(9600);
}

int v;
void loop() {
	v = analogRead(sensor);
	Serial.println("valor = " + String(v));
	delay(500);
}
*/