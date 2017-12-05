cmake_minimum_required(VERSION 2.8.3)
project(houseapi)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roscpp
  std_msgs
)

###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS rospy std_msgs
)

###########
## Build ##
###########

include_directories(${catkin_INCLUDE_DIRS})

