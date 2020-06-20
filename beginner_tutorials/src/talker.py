#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    # 퍼블리셔 선언, 본 node는 chatter라는 topic을
    # String.String 메시지 타입기반으로 퍼블리싱 한다.
    # 퍼블리셔큐(queue) 사이즈를10개로 설정. 
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # 가장 중요한 부분. 본 node의 이름을 talker라고 설정하며, 이 정보는 rospy가 취득함.
    # rospy가 이 정보를 얻기 전까지는 ROS master와 통신이 시작되지 않음.
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():  #사용자가 Ctrl++C를 누르기 전까지 반복
        # 지정된 string 구문에 시간 정보를 붙여서 str이라는 변수 저장.
        hello_str = "hello world %s" % rospy.get_time()
        # console 화면에 print 하고, node의 log에 기록하며, rosout에 기록한다.
        rospy.loginfo(hello_str)
        # chatter topic에게 지정된 string 구문을 퍼블리싱 한다.
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass