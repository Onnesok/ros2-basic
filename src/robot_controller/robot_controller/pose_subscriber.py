#!/usr/bin/env python3

#This is a subscriber node

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class pose_subscriber_node(Node):
    
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(
            Pose, "turtle1/pose", self.pose_callback, 10
        )

    def pose_callback(self, msg: Pose):
        self.get_logger().info("( x data = " + str(msg.x) + ",  y data =" + str(msg.y) + ")")



def main(args = None):
    rclpy.init(args=args)
    node = pose_subscriber_node()
    rclpy.spin(node)

    rclpy.shutdown()



if __name__ == '__main__':
    main()
    