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
	myfile.open("servoData.txt", std::ofstream::out | std::ofstream::app);
	dynamixel_msgs::MotorState servo0 = state->motor_states[0];
	myfile << servo0.position << ", " << servo0.speed  << ", " << servo0.load << ", "<< ros::Time::now() << endl;
	myfile.close();
}

int main(int argc, char **argv) {
	ros::init(argc, argv, "talker");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("/motor_states/pan_tilt_port", 1,servoDataCallback);

	int counter = 0;
	bool endtest = false;
	double u = 1.5, val = 0.0, step = 0.05, amplitude = 2, frequency = 100.0;

	ros::Rate loop_rate(frequency); // 10Hz loop
	std_msgs::Float64 speedMsg;
	speedMsg.data = u;

	ofstream myfile;
	myfile.open("servoData.txt", std::ostream::trunc);
	myfile.close();

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
		myfile << u << ", " << ros::Time::now() << endl;
		ros::spinOnce();
		loop_rate.sleep();
	}

	

	speedMsg.data = 0;
	speed_pub.publish(speedMsg);	

	cout << "loop terminated \n";
	myfile.close();

	return 0;
}
