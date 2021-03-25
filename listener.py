#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from datetime import datetime

def callback(data):
	cdt=datetime.now()
	msg = "%s %s:%s:%s" % (data.data,cdt.hour,cdt.minute,cdt.second)
	rospy.loginfo(msg)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
