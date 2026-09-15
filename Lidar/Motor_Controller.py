import serial
import time

class MotorController:

    def __init__(self, baudrate=115200, port="/dev/ttyACM0"):
        self.baudrate = baudrate
        self.port = port
        self.serial_connection = serial.Serial(port, baudrate, timeout=1)
    
    def send_command(self, command):
        if self.serial_connection.is_open:
            self.serial_connection.write(command.encode())
            time.sleep(0.1) 
            response = self.serial_connection.readline().decode().strip()
            return response
        else:
            raise Exception("Serial connection is not open.")




def main():
    motor_controller = MotorController()
    response = motor_controller.send_command("G0 X10 Y10 Z10") 
    print(f"Motor response: {response}")


if __name__ == "__main__":
    main()