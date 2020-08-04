#!/usr/bin/env python
import sensor_msgs.point_cloud2 as pc2
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
import laser_geometry.laser_geometry as lg
import math

import numpy as np
import ros_numpy
from ros_numpy import numpy_msg

rospy.init_node("laserscan_to_pointcloud")

lp = lg.LaserProjection()

pc_pub = rospy.Publisher("converted_pc", PointCloud2, queue_size=1)

def scan_cb(msg):
    # convert the message of type LaserScan to a PointCloud2
    pc2_msg = lp.projectLaser(msg)

    data = ros_numpy.numpify(pc2_msg)
    print(np.info(data))
    # now we can do something with the PointCloud2 for example:
    # publish it
    pc_pub.publish(pc2_msg)

rospy.Subscriber("/scan", LaserScan, scan_cb, queue_size=1)
rospy.spin()

