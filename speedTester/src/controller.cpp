#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "dynamixel_msgs/MotorStateList.h"

#include <sstream>
#include <iostream>
#include <fstream>
using namespace std;



int main(int argc, char **argv) {
	ros::init(argc, argv, "speedCTR");
	ros::NodeHandle n;
	
	int counter = 0;
	bool endtest = false;
	double u =0, val = 0.0, amplitude = 2;
	// 100hz 0.035step; 10hz 0.35step; 7hz 0.5step; 20hz 0.175step
	double frequency = 100.0, step = 0.00448798950512828;

	ros::Rate loop_rate(frequency); // 10Hz loop
	std_msgs::Float64 speedMsg;
	speedMsg.data = u;

	ofstream myfile;
	myfile.open("servoControl.txt", std::ostream::trunc);
	myfile.close();
	myfile.open("servoControl.txt", std::ostream::app | std::ofstream::out);


	ros::Publisher speed_pub = n.advertise<std_msgs::Float64>(
				"/pan_controller/command", 1, false);
	ros::Time beginT = ros::Time::now();

	while (ros::ok())
	{
		counter++;
		val += step;
		u = amplitude*sin(val);
		speedMsg.data = u;
		//if (ros::Time::now() >= beginT + ros::Duration(2.0))
		//	speedMsg.data = 0.0;	
		speed_pub.publish(speedMsg);
		myfile << u <<", " << val << ", " << ros::Time::now() << endl;
		ros::spinOnce();
		loop_rate.sleep();
	}

	

	speedMsg.data = 0;
	speed_pub.publish(speedMsg);	
	ros::spinOnce();
	loop_rate.sleep();

	cout << "loop terminated \n";
	myfile.close();

	return 0;
}
