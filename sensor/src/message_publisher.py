#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from common_msgs.msg import Message

rospy.init_node('message_publisher')
pub = rospy.Publisher('sensor', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Pose2D(x=second%4, y=second%7, theta=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()
