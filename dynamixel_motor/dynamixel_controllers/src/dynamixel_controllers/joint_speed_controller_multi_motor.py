# -*- coding: utf-8 -*-
#
# Software License Agreement (BSD License)
#
# Copyright (c) 2010-2011, Antons Rebguns.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of University of Arizona nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from __future__ import division


__author__ = 'Elod Pall'
__copyright__ = 'Copyright (c) 2016-2017 Elod Pall'
__credits__ = 'Antons Rebguns and Cara Slutter'

__license__ = 'BSD'
__maintainer__ = 'Elod Pall'
__email__ = 'pall.elod@gmail.com'

from threading import Thread
import rospy


from dynamixel_driver.dynamixel_const import *
# from dynamixel_controllers.joint_controller import JointController
from dynamixel_msgs.msg import JointState
from dynamixel_msgs.msg import MotorVelocityArray

class Segment():
    def __init__(self, num_joints):
        self.start_time = 0.0  # controlled velocity segment start time
        self.duration = 0.0  # applied velocity segment duration
        self.positions = [0.0] * num_joints
        self.velocities = [0.0] * num_joints

class MultiJointSpeedController():
    def __init__(self, controller_namespace, controllers):
        self.update_rate = 1000
        self.state_update_rate = 50
        self.trajectory = []
        
        # parsing each joint name 
        self.controller_namespace = controller_namespace
        self.joint_names = [c.joint_name for c in controllers]
        
        # controller description with all the parameters for a joint 
        self.joint_to_controller = {}
        self.joint_to_ID = {}
        for c in controllers:
            self.joint_to_controller[c.joint_name] = c
            
        
        # adding a namespace for joints? but why?    
        self.port_to_joints = {}
        for c in controllers:
            if c.port_namespace not in self.port_to_joints: self.port_to_joints[c.port_namespace] = []
            self.port_to_joints[c.port_namespace].append(c.joint_name)
        
        # where/for what it is used
        self.port_to_io = {}
        for c in controllers:
            if c.port_namespace in self.port_to_io: continue
            self.port_to_io[c.port_namespace] = c.dxl_io
                            
        # initial joint states    
        self.joint_states = dict(zip(self.joint_names, [c.joint_state for c in controllers]))
        # number of joints
        self.num_joints = len(self.joint_names)
        # mapping joint names and motor IDs
        self.joint_to_idx = dict(zip(self.joint_names, range(self.num_joints)))
        
    def initialize(self):       
        self.loop_frequency_constraint = 1/7
        print "***Controller namespace: " + self.controller_namespace
        return True

    def stop(self):
        self.running = False


    def start(self):
        self.running = True        
        self.command_sub = rospy.Subscriber(self.controller_namespace + '/command', MotorVelocityArray, self.process_command)
        print "***Muti controller started"
        
    def process_command(self, msg):  
                
        vals = []
        print "***msg received: "
        
        if len(msg.joint_name) > len(self.joint_names):
            print "Control massage has more joints than controllers"
            return False
        
        for i in  range(len(msg.joint_name)):
           joint = msg.joint_name[i]
           vel_rad = msg.vel_cmd[i]
           print "joint: '" + joint + "' velocity= " + str(vel_rad)
            
            # check if motor ID in IDs list            
           if joint not in self.joint_names:
               print "Given joint " + joint + " not found in controllers list: " 
               print self.joint_names
               return False
           
           motorID = self.joint_to_controller[joint].motor_id  
           
           vel_raw = self.joint_to_controller[joint].spd_rad_to_raw(vel_rad)
           print "motor ID = " + str(motorID) + "raw value = " + str(vel_raw);
           
           vals.append((motorID, vel_raw))
            
        for port, io in self.port_to_io.items():
            print "sent to port:" + port + " io " + io.port_name  
            io.set_multi_speed(vals)
            break
        
            
            
            
            
            
            
            
            
            
            