#!/usr/bin/env python3
import rospy

from pyscript import document

from std_msgs.msg import UInt16

tekst0 = document.querrySelector

def pose_callback(msg: UInt16):
    position = str(msg)
    rospy.loginfo("position: " + position)

if __name__ == '__main__':
    rospy.init_node("current_position")

    sub = rospy.Subscriber("/virtual_dc_motor_node/get_position_0", UInt16, callback=pose_callback)

    rospy.loginfo("subscriber is working")
    rospy.spin()