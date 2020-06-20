#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    # rospy에게 본 node의 이름을 알려줌. 마찬가지로, rospy가 이 정보를 얻기 전 까지는
    # ROS Master와 통신은 시작 되지 않는다. 
    # anonymous 옵션을 true로 하면, 본 노드를 복수로 실행 가능하다.
    rospy.init_node('listener', anonymous=True)
    # 본 노드가 std_msgs.msgs.Sting 타입의 메시지를 chatter topic으로부터 구독함.
    # 새로운 메시지가 수신 받았을때,, callback 함수는 그 메시지를 첫번째 변수로 불러옴.
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()