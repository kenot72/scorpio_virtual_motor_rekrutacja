#!/usr/bin/env python3
import rospy

import sys
import termios
import tty

from select import select

from std_msgs.msg import Int8

def saveTerminalSettings():
    return termios.tcgetattr(sys.stdin)

def if_key_pushed_move(key, var, char1, char2, motor):
    if key == char1 and var > -100:
        rospy.loginfo("motor " + str(motor) + ": " + str(var-1))
        return var-1
    elif key == char2 and var < 100:
        rospy.loginfo("motor " + str(motor) + ": " + str(var+1))
        return var+1
    else:
        return var

def getKey(settings, timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__ == '__main__':
    rospy.init_node("motor_control")
    rospy.loginfo("Motor 0:\n left control q \n right control: e\nMotor 1:\n left control a \n right control: d\nMotor 2:\n left control z \n right control: c\n To disable/enable Motor control: b")

    settings = saveTerminalSettings()
    key_timeout = rospy.get_param("~key_timeout", 0.5)

    pub0 = rospy.Publisher("virtual_dc_motor_node/set_cs_0", Int8, queue_size=10)
    pub1 = rospy.Publisher("virtual_dc_motor_node/set_cs_1", Int8, queue_size=10)
    pub2 = rospy.Publisher("virtual_dc_motor_node/set_cs_2", Int8, queue_size=10)

    x0 = 0
    x1 = 0
    x2 = 0

    state = True

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        key = getKey(settings, key_timeout)

        if key == 'b':
            if state == True:
                state = False
                rospy.loginfo("Motor control: disabled")
            else:
                state = True
                rospy.loginfo("Motor control: enabled")
        if state == True:
            msg0 = Int8()
            msg1 = Int8()
            msg2 = Int8()
            if key != '':
                x0 = if_key_pushed_move(key, x0, 'q', 'e', 0)
                x1 = if_key_pushed_move(key, x1, 'a', 'd', 1)
                x2 = if_key_pushed_move(key, x2, 'z', 'c', 2)
            msg0.data = x0
            msg1.data = x1
            msg2.data = x2
            pub0.publish(msg0)
            pub1.publish(msg1)
            pub2.publish(msg2)
        
        rate.sleep()