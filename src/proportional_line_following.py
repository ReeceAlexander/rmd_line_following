#!/usr/bin/env python3

import rospy
import os

from rmd_line_following.msg import LineOrientation

os.system("sudo ip link set can0 down")
rospy.sleep(0.1)
os.system("sudo ip link set can0 up type can bitrate 1000000")

offset = 0.0
deviation = 0.0

def moveForward():
    print("hello")

def moveBackward():
    print("hello")

def turnLeft():
    print("hello")

def turnRight():
    print("hello")

def slideLeft():
    print("hello")

def slideRight():
    print("hello")

def stop():
    print("hello")

def callback(msg):
    upper_threshold = 0.1
    lower_threshold = -0.1
    
    if msg.offset > upper_threshold:
        slideLeft()

    elif msg.offset < lower_threshold:
        slideRight()

    else:
        moveForward()

    if msg.deviation > upper_threshold:
        turnLeft()

    elif msg.deviation < lower_threshold:
        turnRight()

    else:
        moveForward()
        


def main():
    rospy.init_node("p_line_following_node")

    rospy.Subscriber('/line_position', LineOrientation, callback, queue_size=1)

    rospy.spin()

if __name__ == "__main__":
    main()