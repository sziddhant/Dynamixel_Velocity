rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 0
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 1
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 2
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 3
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 4
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 5
rosrun dynamixel_driver set_servo_config.py --port=/dev/ttyUSB0 -b 1000000 --cw-angle-limit=0 --ccw-angle-limit=0 6
rosrun dynamixel_driver info_dump.py --port=/dev/ttyUSB0 --baud=1000000 0 1 2 3 4 5 6 7 
