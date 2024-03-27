#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import UInt16

def callback0(msg: UInt16):
    position = str(msg)
    rospy.loginfo("position: " + position)
    res = [int(i) for i in position.split() if i.isdigit()]
    for x in res:
        rospy.loginfo("pozycja 0:" + str(round(x/(4096/360),2)))
    time.sleep(1)
    

def callback1(msg: UInt16):
    position = str(msg)
    res = [int(i) for i in position.split() if i.isdigit()]
    for x in res:
        rospy.loginfo("pozycja 1:" + str(round(x/(4096/360),2)))
    time.sleep(1)
    
def callback2(msg: UInt16):
    position = str(msg)
    res = [int(i) for i in position.split() if i.isdigit()]
    for x in res:
        rospy.loginfo("pozycja 2:" + str(round(x/(4096/360),2)))
    time.sleep(1)
    
    
if __name__ == '__main__':
    rospy.init_node("current_position")
    rospy.loginfo("subscriber is working")

    sub0 = rospy.Subscriber("/virtual_dc_motor_node/get_position_0", UInt16, callback=callback0)
    sub1 = rospy.Subscriber("/virtual_dc_motor_node/get_position_1", UInt16, callback=callback1)
    sub2 = rospy.Subscriber("/virtual_dc_motor_node/get_position_2", UInt16, callback=callback2)

    rospy.spin()