#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud

def callback(data):
    rospy.loginfo("Points are here!")

def listener():
    rospy.init_node("listener")
    rospy.Subscriber("points", PointCloud, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
