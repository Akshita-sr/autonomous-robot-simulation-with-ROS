#!/usr/bin/env python3
# Import the necessary libraries

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
def robot_controller():
    rospy.init_node('robot_controller', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    lidar_subscriber = rospy.Subscriber('/scan', LaserScan, lidar_callback)
    rospy.spin()
velocity_publisher = None

def lidar_callback(msg):
    # Define the vel_msg variable
    vel_msg = Twist()
    # Check if there is an obstacle in front of the robot
    if min(msg.ranges) < 1.0:
        # If there is an obstacle, stop the robot
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 0.0
    else:
        # If there is no obstacle, move the robot forward
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.0
    # Publish the velocity command
    velocity_publisher.publish(vel_msg)

def robot_controller():
    global velocity_publisher
    rospy.init_node('robot_controller', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    lidar_subscriber = rospy.Subscriber('/scan', LaserScan, lidar_callback)
    rospy.spin()
if __name__ == '__main__':
    robot_controller()
