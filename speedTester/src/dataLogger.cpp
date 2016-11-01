#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "dynamixel_msgs/MotorStateList.h"

#include <sstream>
#include <iostream>
#include <fstream>
using namespace std;

void servoDataCallback(const dynamixel_msgs::MotorStateList::ConstPtr& state) //std_msgs::String::ConstPtr& msg)
		{
	ofstream myfile;
	myfile.open("servoDataTauTest.txt", std::ofstream::out | std::ofstream::app);
	dynamixel_msgs::MotorState servo0 = state->motor_states[0];
	myfile << servo0.position << ", " << servo0.speed  << ", " << servo0.goal << ", "<< ros::Time::now() << endl;
	myfile.close();
}

int main(int argc, char **argv) {
	ros::init(argc, argv, "speedLog");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("/motor_states/tau_port", 1,servoDataCallback);

	double frequency = 100.0;
	ros::Rate loop_rate(frequency);

	ofstream myfile;
	myfile.open("servoData.txt", std::ostream::trunc);
	myfile.close();
	cout << "Servo Data logging started \n";

	while (ros::ok())
	{
		ros::spinOnce();
		loop_rate.sleep();
	}
	cout << "Logging terminated \n";
	return 0;
}
