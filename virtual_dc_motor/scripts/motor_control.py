#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8

if __name__ == '__main__':
    rospy.init_node("motor_control")
    rospy.loginfo("Node has been started")


    pub = rospy.Publisher("virtual_dc_motor_node/set_cs_0", Int8, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Int8()
        msg.data = 20
        pub.publish(msg)
        
        rate.sleep()