rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=4095 0
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=855 --ccw-angle-limit=3245 1
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=855 --ccw-angle-limit=3245 2
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=855 --ccw-angle-limit=3245 3
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=855 --ccw-angle-limit=3245 4
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=855 --ccw-angle-limit=3245 5
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=4095 6
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=1578 --ccw-angle-limit=3172 7
rosrun dynamixel_driver info_dump.py --port=/dev/ttyUSB0 --baud=1000000 0 1 2 3 4 5 6 7 
