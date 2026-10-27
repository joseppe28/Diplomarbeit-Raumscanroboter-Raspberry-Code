// X driver
#define X_STEP_PIN    54
#define X_DIR_PIN     55
#define X_ENABLE_PIN  38

// Y driver
#define Y_STEP_PIN    60
#define Y_DIR_PIN     61
#define Y_ENABLE_PIN  56

// Z driver
#define Z_STEP_PIN    46
#define Z_DIR_PIN     48
#define Z_ENABLE_PIN  62

void setup() {
  Serial.begin(115200);


  pinMode(X_STEP_PIN, OUTPUT);
  pinMode(X_DIR_PIN, OUTPUT);
  pinMode(X_ENABLE_PIN, OUTPUT);

  pinMode(Y_STEP_PIN, OUTPUT);
  pinMode(Y_DIR_PIN, OUTPUT);
  pinMode(Y_ENABLE_PIN, OUTPUT);

  pinMode(Z_STEP_PIN, OUTPUT);
  pinMode(Z_DIR_PIN, OUTPUT);
  pinMode(Z_ENABLE_PIN, OUTPUT);

  // Hier die Motoren Enablen LOW = Enabled
  digitalWrite(X_ENABLE_PIN, LOW);
  digitalWrite(Y_ENABLE_PIN, LOW);
  digitalWrite(Z_ENABLE_PIN, LOW);

  // Die Richtung angeben
  digitalWrite(X_DIR_PIN, HIGH);
  digitalWrite(Y_DIR_PIN, HIGH);
  digitalWrite(Z_DIR_PIN, HIGH);
}

void loop() {
  manage_command();
}

String get_command() {
  if (Serial.available() > 0) {
    return Serial.readStringUntil('\n');
  }

  return "";
}


/*
    Command structure:

    First 1-2 Letters are the function which i want to call
    L --> Move the Lidar controller
    M --> Move the whole roboter
    MT --> Move to function
    ...

    After that is a ;

    Then there are the paramters of the to be called function
    like for exmaple
    L;1 --> moves lidar motor by 1 step
    M;5 --> Moves the Roboter 5 Steps forward

    If i need more than one paramter they are speratared by spaces
    MT;10 10 --> Would move him in more than one axis
*/


// Receives the Command from the Pi and calls the right function
// Parameter: None
// Return : True or False / It worked or didnt work
bool manage_command() {
  String command = get_command();

  if (command == "") {
    return false;
  }
  Serial.println(command);
  int dividerIndex = command.indexOf(";");
  String function = command.substring(0, dividerIndex);

  if (function == "L") {
    int paramter = command.substring(dividerIndex + 1).toInt();
    move_lidar_motor(paramter);
  }

}


// Function to spin the lidar motor to later get another slice of the room
// Parameter: The steps the Lidar motor should make
// Return : None
void move_lidar_motor(int steps) {
  Serial.print("Test Steps taken: ");
  Serial.println(steps);
  for (int i = 0; i < steps; i++) {
    digitalWrite(Z_STEP_PIN, HIGH);
    delayMicroseconds(500);

    digitalWrite(Z_STEP_PIN, LOW);
    delayMicroseconds(500);

  }
}
