#!/usr/bin/env python
## Dynamixel Velocity control in ROS using python

import rospy
from dynamixel_msgs.msg._MotorVelocityArray import MotorVelocityArray
def motorVel(j1,j2):
    pub = rospy.Publisher('multi_joint_speed_controller/command',  MotorVelocityArray, queue_size=10)
    rospy.init_node('PythonController', anonymous=True)
    vel=MotorVelocityArray()
    vel.joint_name=["joint1","joint2"]
    vel.vel_cmd= [j1,j2]
    pub.publish(vel)


if __name__ == '__main__':
    try:
        motorVel(0,0)
    except rospy.ROSInterruptException:
        pass