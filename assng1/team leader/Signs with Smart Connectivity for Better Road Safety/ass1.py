void setup()
{

pinMode(3, INPUT); pinMode(13, OUTPUT);

}

void loop()

{
If (digitalRead(3) == HIGH) { digitalWrite(13, HIGH);
} else {
digitalWrite(13, LOW);
}
delay(10); // Delay a little bit to improve simulation performance 
}
