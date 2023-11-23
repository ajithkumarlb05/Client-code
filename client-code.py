#include <ESP8266WiFi.h>
#include <WiFiClient.h>

// Wi-Fi settings
const char* ssid = "XXX";
const char* password = "XXX";

// Server settings
const char* server_ip = "XXX";  // Replace with your server's IP address
const int server_port = XXX;             // Replace with your server's port number

// EMG sensor pin
const int emg_pin = A0;

// Valid EMG data range
const int emg_data_min = 0;
const int emg_data_max = 1023;

// Initialize Wi-Fi client
WiFiClient client;

// Connect to Wi-Fi
void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

// Start sending EMG data to server
void send_data() {
  int emg_data = analogRead(emg_pin);
  if (emg_data >= emg_data_min && emg_data <= emg_data_max) {
    // Validate EMG data
    if (!client.connected()) {
      // If client is not connected, attempt to reconnect
      client.connect(server_ip, server_port);
    }
    if (client.connected()) {
      // If client is connected, send EMG data
      client.print(emg_data);
    } else {
      // If client is not connected, delay before retrying
      delay(1000);
    }
  } else {
    // Invalid EMG data, skip sending and delay
    delay(1000);
  }
}

void setup() {
  Serial.begin(9600);
  setup_wifi();
}

void loop() {
  send_data();
  delay(100);
}
