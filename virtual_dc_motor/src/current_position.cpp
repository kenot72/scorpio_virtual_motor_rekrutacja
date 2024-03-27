#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/UInt16.h"

void positionCallback(const std_msgs::UInt16::ConstPtr& msg)
{
    ROSINFO("position = %u", msg->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc,argv, "current_position");

    ros::NodeHandle n;

    ros::Subscriber sub = n.subscribe("/virtual_dc_motor_node/get_position_0", 20, positionCallback);

    ros::spin();

    return 0;
}