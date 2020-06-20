#!/usr/bin/env python  
# -*- coding: UTF-8 -*-
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')
    # 아래와 같이 tf listener object를 생성할 경우, tf 변환 행렬을 계속 받는다.
    # 최대 10초까지 버퍼링한다.
    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(4, 2, 0, 'turtle2')

    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)
    
    # tf.TransformListener()에서 받아온 tf 변환 행렬 중, 특정 좌표계 간의 변환 행렬을 list에 저장한다.
    # '/turtle2' 좌표계를 기준으로 '/turtle1' 좌표계의 변환 행렬 반환.
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
               # trans = (x, y, z), rot = (x, y, z, w)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()