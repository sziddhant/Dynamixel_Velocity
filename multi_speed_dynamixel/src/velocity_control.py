#!/usr/bin/env python3

import rospy
from dynamixel_msgs.msg._MotorVelocityArray import MotorVelocityArray
def talker():
    pub = rospy.Publisher('multi_joint_speed_controller/command',  MotorVelocityArray, queue_size=10)
    rospy.init_node('PythonController', anonymous=True)
    r = rospy.Rate(10) #10hz
    
    while not rospy.is_shutdown():
        vel=MotorVelocityArray()
        vel.joint_name=["joint1","joint2"]
        vel.vel_cmd= [0,0]
        pub.publish(vel)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass