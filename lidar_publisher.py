#!/usr/bin/env python3
from random import randint
import rospy
from sensor_msgs.msg import PointCloud, ChannelFloat32
from geometry_msgs.msg import Point32

def publisher():
    pub = rospy.Publisher("points", PointCloud, queue_size=50)
    rospy.init_node("lidar")
    rate = rospy.Rate(1)
    count = 0
    while not rospy.is_shutdown():
        count += 1
        cloud = PointCloud()
        channel = ChannelFloat32()
        cloud.header.seq = count
        cloud.header.stamp = rospy.Time.now()
        cloud.header.frame_id = "sensor_frame"

        for i in range(3):
            point = Point32()
            point.x = randint(0,10)
            point.y = randint(0,10)
            point.z = randint(0,10)
            
            cloud.points.append(point)

        channel.name = "intensity"

        intensities = []
        for i in range(3):
            intensities.append(randint(0,10))

        channel.values = intensities
        cloud.channels.append(channel)

        pub.publish(cloud)
        rospy.loginfo(cloud)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
