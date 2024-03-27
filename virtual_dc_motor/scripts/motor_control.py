#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8

if __name__ == '__main__':
    rospy.init_node("motor_control")
    rospy.loginfo("Node has been started")


    pub0 = rospy.Publisher("virtual_dc_motor_node/set_cs_0", Int8, queue_size=10)
    pub1 = rospy.Publisher("virtual_dc_motor_node/set_cs_1", Int8, queue_size=10)
    pub2 = rospy.Publisher("virtual_dc_motor_node/set_cs_2", Int8, queue_size=10)


    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg0 = Int8()
        msg1 = Int8()
        msg2 = Int8()
        msg0.data = 20
        msg1.data = -40
        msg2.data = 80
        pub0.publish(msg0)
        pub1.publish(msg1)
        pub2.publish(msg2)
        
        rate.sleep()