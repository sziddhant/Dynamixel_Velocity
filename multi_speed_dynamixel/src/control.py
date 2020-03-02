#!/usr/bin/env python
## Dynamixel Velocity control in ROS using python

import rospy
from dynamixel_msgs.msg._MotorVelocityArray import MotorVelocityArray
def motorVel(j1,j2,j3,j4,j5,j6):
    pub = rospy.Publisher('multi_joint_speed_controller/command',  MotorVelocityArray, queue_size=10)
    rospy.init_node('PythonController', anonymous=True)
    #r = rospy.Rate(10) #10hz
    vel=MotorVelocityArray()
    vel.joint_name=["joint1","joint3"]
    vel.vel_cmd= [j1,j2,j3,j4,j5,j6]
    pub.publish(vel)
    #print('11')
    #r.sleep()

if __name__ == '__main__':
    try:
        
        motorVel(0,0,0,0,0,0)
        r = rospy.Rate(5) #10hz
        r.sleep()
        motorVel(1,1,1,1,1,1)
        r.sleep()
        print('hi')
        motorVel(10,10,10,10,10,10)
        r.sleep()
        motorVel(0,0,0,0,0,0)
    except rospy.ROSInterruptException:
        pass