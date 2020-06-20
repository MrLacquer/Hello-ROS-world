# Hello ROS world (melodic)

## Overview

This repository is for the ROS study.  

- Ref. 01: [Writing a Simple Publisher and Subscriber (Python)](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
- Ref. 02: [tf/Tutorial](http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29)  

The packages have been tested under ROS Melodic and Ubuntu 18.04, 


**Author: [Hyeonjun Park](https://www.linkedin.com/in/hyeonjun-park-41bb59125), koreaphj91@gmail.com**

**Affiliation: [Human-Robot Interaction LAB](https://khu-hri.weebly.com), Kyung Hee Unviersity, South Korea**
<!--
![hj_object dectect: Detection image](https://user-images.githubusercontent.com/4105524/63675994-008b8700-c825-11e9-84fb-1be015bc3be6.png)
-->

## Installation
- Before do this, please backup important files.

### Dependencies

This software is built on the Robotic Operating System ([ROS](http://wiki.ros.org/ROS/Installation)).

for Desktop
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
``` 
after ROS install
```
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc 
$ source ~/.bashrc

$ sudo apt install python-rosdep 
$ sudo rosdep init 
$ rosdep update
```
setup workspace 
```
$ mkdir catkin_ws 
$ cd catkin_ws 
$ mkdir src 
$ cd src 
$ catkin_ws && catkin_make
```
setup shortcuts
```
$ gedit ~/.bashrc 
      alias eb='gedit ~/.bashrc' 
      alias sb='source ~/.bashrc' 
      alias cw='cd ~/catkin_ws' 
      alias cs='cd ~/catkin_ws/src' 
      alias cm='cd ~/catkin_ws && catkin_make' 

      source /opt/ros/melodic/setup.bash 
      source ~/catkin_ws/devel/setup.bash 

$ source ~/.bashrc
```
Reference [ROS Melodic Install, humine](https://blog.naver.com/humine/221906137469)


## Note



