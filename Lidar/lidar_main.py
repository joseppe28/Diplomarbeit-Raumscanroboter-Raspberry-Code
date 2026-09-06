import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarNode(Node):

    def __init__(self):
        super().__init__('lidar_node')

        self.cloud = {}

        self.subscription = self.create_subscription(
            LaserScan,
            "/scan",
            self.receive_data,
            10
        )
    
    # is called when data is received and calls the converter 
    # Parameter: self, the message received from the LIDAR
    # Return: None
    def receive_data(self, msg):
        self.get_logger().info(f"Received LIDAR data: {msg.ranges}")

        # Convert LIDAR data to Cartesian coordinates
        converter = LidarDataConverter()
        self.cloud = converter.convert_to_3d_Cloud(
            msg.ranges,
            msg.intensities,
            msg.angle_min,
            msg.angle_increment,
            0  # Replace with actual motor angle if available
        )

        self.get_logger().info(f"Converted to Cartesian: {self.cloud}")


class LidarDataConverter():
    
    def __init__(self):
        pass

    # Converts the LIDAR data to a dictionary with teh coordinates and the accuracy 
    # Parameters: self, the range data, the accuracy of the points,  the minimum / start angel, the angel increment of each scan, the current angle of the motor
    # Return: a dictionary with the coordinates and the accuracy of each point
    def convert_to_3d_Cloud(self, ranges, intensities, angle_min, angle_increment, motor_angle):
        cloud = {}
        for r, a in zip(ranges, intensities):
            angle = angle_min + ranges.index(r) * angle_increment
             
            # Zuerst ein Dreick in der X-Z Ebende um Z und eine hilfvariable d zu berechnen
            z = r * math.sin(angle)
            d = r * math.cos(angle)

            # mit d in der X-Y Ebene die fehlenden zwei Koordinaten berechnen 
            x = d * math.cos(motor_angle)
            y = d * math.sin(motor_angle)

            cloud[(x, y, z)] = a 

        return cloud




def main():
    rclpy.init()

    node = LidarReader()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()