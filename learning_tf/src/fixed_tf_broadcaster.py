#!/usr/bin/env python  
# -*- coding: UTF-8 -*-

import roslib
roslib.load_manifest('learning_tf')

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    # 새로운 tf 를 생성함. turtle1을 parent frame으로 해서 carrot1이라는 
    # child frame을 생성함. carrot1 frame은 turtle1 frame에서 2m offset.
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 2.0, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "carrot1",
                         "turtle1")
        rate.sleep()