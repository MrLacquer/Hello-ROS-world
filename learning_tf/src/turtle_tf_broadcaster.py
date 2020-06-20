#!/usr/bin/env python  
# -*- coding: UTF-8 -*-
import roslib
roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):    
    # 'world' 좌표계를 기준으로 한 'turtleX' 의 변환 행렬을 퍼블리시 한다.
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')      
    #본 노드는 터틀봇 이름(예: "turtle1" 또는 "turtle2")을 지정하는 단일 매개변수 "~turtle"을 사용한다.
    # launch 파일에서 사용하는 param name="turtle" 에서 직접 이름을 지정한다.
    turtlename = rospy.get_param('~turtle')
    # "turtleX/pose" 의 토픽을 서브스크라이브 한다.
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()