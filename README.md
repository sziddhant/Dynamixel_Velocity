# Velocity controller for Dynamixel motors in ROS

This repository contains ROS packages to control dynamixel motors with velocity commands. It was tested on AX12-A, MX-28, and MX-64 motors. Tested with ROS Kinetic on Ubuntu 16.04. This pkg is a modified version of Dynamixel Velocity Controller by Előd Páll
## Package Overview 

*velocity driver*: It is a modified dynamixel motor driver ([original source](https://github.com/arebgun/dynamixel_motor)), extended with a velocity controller for a single motor using `joint_speed_controller.py` and one for controlling multiple motor's velocities `joint_speed_controller_multi_motor.py`. The second one sends the command for each motor at the same time. This requires a spacial massage that contains two vector one with motor names and another with velocity cmd values, see `MotorVelocityArray.msg`. 
The motors must be in wheel mode (cw and ccw are set to 0). As this pkg collection is used on a robot arm where we have physical joint angle limits, we introduced a new parameter for upper and lower angle limits: `maxAngle` and `minAngle`. If the two parameters are equal, then the driver wont have any angle limitations so the motor can spin continuously.

**multi_speed_dynamixel**: this creates the velocity control spanner and manager nodes, there is an examples for two motors. Note that the joint specification sets obligatory `min: 0` and `max: 0`, so the motors are used in wheel mode. Use `minAngle` and `maxAngle` to set joint angle limits. 

## Usage ##

Set motors to wheel mode.
Start the two motor controller:

```
$ roslaunch multi_speed_dynamixel speed_controller_motors.launch
```

Publish a command velocity msg for two motors:

```
$ rostopic pub -1 /multi_joint_speed_controller/command dynamixel_msgs/MotorVelocityArray "{joint_name:['wrist_roll_joint', 'wrist_pitch_joint'], vel_cmd:[-0.2, 0.1]}"
```
**Note**: after publishing a velocity command, the motor will rotate at the requested speed until receives another command or reaches an angle limit. If the motor is going to be used in position control, change CW and CCW values from (0,0) to the original one. 

