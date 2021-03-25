#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def speaker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('speaker', anonymous=True)
    while not rospy.is_shutdown():
    	name=input()
    	rospy.loginfo(name)
    	pub.publish(name)

if __name__ == '__main__':
    try:
        speaker()
    except rospy.ROSInterruptException:
        pass
