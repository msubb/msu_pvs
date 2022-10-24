/* Arduino 256 RGB LEDs Matrix Animation Frame
   Using WS2812 LED Strips

  Created by Yvan / https://Brainy-Bits.com

  This code is in the public domain...

  You can: copy it, use it, modify it, share it or just plain ignore it!
  Thx!

*/

String incomingByte ;


#include <avr/pgmspace.h>  // Needed to store stuff in Flash using PROGMEM
#include "FastLED.h"       // Fastled library to control the LEDs

// How many leds are connected?
#define NUM_LEDS 64

// Define the Data Pin
#define DATA_PIN 5  // Connected to the data pin of the first LED strip

// Define the array of leds
CRGB leds[NUM_LEDS];

// Create the array of retro arcade characters and store it in Flash memory
const long ledarray0[] PROGMEM = {
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00FFFFFF, 
        0x00FFFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
};

const long ledarray1[] PROGMEM = {
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
        0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
};

const long ledarray2[] PROGMEM = {
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 
        0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
};

const long ledarray3[] PROGMEM = {
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 
        0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 
        0x00000000, 0x00FFFFFF, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00000000, 0x00FFFFFF, 0x00FFFFFF, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
        0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
};


void setup() {
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS); // Init of the Fastled library
  FastLED.setBrightness(1);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');
    delay(1000);

    if (incomingByte == "zero") {

      FastLED.clear();
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = pgm_read_dword(&(ledarray0[i]));  // Read array from Flash
      }
      FastLED.show();

      Serial.write("Led 0");

    }

    else if (incomingByte == "1") {

      FastLED.clear();
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = pgm_read_dword(&(ledarray1[i]));  // Read array from Flash
      }
      FastLED.show();

      Serial.write("Led 1");

    }

    else if (incomingByte == "2") {

      FastLED.clear();
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = pgm_read_dword(&(ledarray2[i]));  // Read array from Flash
      }
      FastLED.show();

      Serial.write("Led 2");

    }

    else if (incomingByte == "3") {

      FastLED.clear();
      for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = pgm_read_dword(&(ledarray3[i]));  // Read array from Flash
      }
      FastLED.show();

      Serial.write("Led 3");

    }

    else {

      Serial.write("invald input");

    }

  }







}
