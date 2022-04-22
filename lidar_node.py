#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud, ChannelFloat32
from geometry_msgs.msg import Point32

def publisher():
    pub = rospy.Publisher("points", PointCloud, queue_size=50)
    rospy.init_node("lidar")
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        cloud = PointCloud()
        point = Point32()
        channel = ChannelFloat32()

        cloud.header.stamp = rospy.Time.now()
        cloud.header.frame_id = "sensor_frame"
        
        point.x = 1.2
        point.y = 3.5
        point.z = 2.5

        channel.name = "intensity"
        channel.values = [5.5]

        cloud.points.append(point)
        cloud.channels.append(channel)

      
       

        pub.publish(cloud)
        rospy.loginfo(cloud)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
