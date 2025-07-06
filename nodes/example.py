#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ExampleNode(Node):
  
  def __init__(self):
    super().__init__('nodito')
    self.pub = self.create_publisher(String, "/nodito_talker", 10)
    self.timer = self.create_timer(1, self.talk)

  def talk(self):
    msg = String()
    msg.data = "nodito is alive"
    self.pub.publish(msg)


def main():
  rclpy.init()
  node = ExampleNode()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()



