# Velocity controller for Dynamixel motors in ROS#

This repository contains ROS packages and a Simulink example to control dynamixel motors with velocity commands. It was tested on AX12-A, MX-28, and MX-64 motors. We are using ROS Indigo and Matlab 2015a on Ubuntu 14.04. This pkg is intended to be used on a Cyton Gamma 1500 robot arm.

## PKG overview ##

*velocity driver*: this is a modified dynamixel motor driver ([original source](https://github.com/arebgun/dynamixel_motor)), we extended with a velocity controller for a single motor `joint_speed_controller.py` and one for controlling multiple motor's velocities `joint_speed_controller_multi_motor.py`. The second one sends the command for each motor at the same time. This requires a spacial massage that contains two vector one with motor names and another with velocity cmd values, see `MotorVelocityArray.msg`. 
The motors must be in wheel mode (cw and ccw are set to 0). As this pkg collection is used on a robot arm where we have physical joint angle limits, we introduced a new parameter for upper and lower angle limits: `maxAngle` and `minAngle`. If the two parameters are equal, then the driver wont have any angle limitations so the motor can spin continuously.

*emulated torque drivers*: two torque drivers are added `joint_emulated_torque_controller.py` and `joint_emulated_torque_controllerV2.py`. These drivers are not yet tested and confirmed that they apply approximately the desired torque. Motor and parameter calibration is needed, see reference [publication](http://shervinemami.info/dynamixel_study_by_ett.pdf)

* `joint_emulated_torque_controller.py` emulate torque in �free spin� mode by using velocity control
* `joint_emulated_torque_controllerV2.py` emulate torque in position control by adjusting the max torque limit and the punch (no feedback adjustment is implemented)  

**cyton_multi_speed_dynamixel**: this creates the velocity control spanner and manager nodes, there are two examples one for a single motor and another for two motors. Note that the joint specification sets obligatory `min: 0` and `max: 0`, so the motors are used in wheel mode. Use `minAngle` and `maxAngle` to set joint angle limits. 

**speedTester**: this pkg has two nodes one for sending control massages and another for data logging.

**PID_controlledPosiotioning**: this is a Simulink example of a PID controller. The PID gains are not well tuned, the I gain is 0 because the reference is the position while the command signal is the velocity (the system already has an integrator)

## Usage ##

Set one motor to wheel mode:

```
#!BASH\
$ rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 $MOTOR_ID
```
Change the setup for all the motors on the Cyton Gamma 1500 arm from position to wheel mode or vice-versa by simply running `initMotors_pos.sh` or `initMotors_vel.sh` script respectively.

Start the two motor controller:

```
#!bash
$ roslaunch cyton_multi_speed_dynamixel speed_controller_2motors.launch

```

Run velocity command publisher and data logger:

```
#!bash
$ rosrun speedTester speedTester_crt
$ rosrun speedTester speedTester_log
```

Publish a command velocity msg for two motors:

```
#!bash
$ rostopic pub -1 /cyton_multi_joint_speed_controller/command dynamixel_msgs/MotorVelocityArray "{joint_name:['wrist_roll_joint', 'wrist_pitch_joint'], vel_cmd:[-0.2, 0.1]}"
```
**Note**: after publishing a velocity command, the motor will rotate at the requested speed until receives another command or reaches an angle limit. If the motor is going to be used in position control, change CW and CCW values from (0,0) to the original one. 

## Contact ##
Elod Pall

[website](sites.google.com/view/timecontrol/)