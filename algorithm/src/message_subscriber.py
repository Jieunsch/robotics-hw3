#!/usr/bin/env python
import rospy
from common_msgs.msg import Message

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('message_subscriber')
sub = rospy.Subscriber('algorithm', TimePose, callback)
rospy.spin()
