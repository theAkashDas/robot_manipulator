#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub_f1 = rospy.Publisher('/arm/joint7_position_controller/command', Float64, queue_size=10)
    pub_f2 = rospy.Publisher('/arm/joint8_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        # position = math.pi/2
        
        for position in range(0,10):
            pub_f1.publish(position/100)
            pub_f2.publish(position/100)
            rospy.loginfo(position)
            rate.sleep()
        for position in reversed(range(0,10)):
            pub_f1.publish(position/100)
            pub_f2.publish(position/100)
            rospy.loginfo(position)
            rate.sleep()    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass