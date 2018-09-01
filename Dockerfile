# Base container: ros
FROM ros

# Required Python library
RUN apt-get update && apt-get install -y python-pip && apt-get clean
RUN pip install flask rospy_message_converter

# Create workspace and copy required files
RUN mkdir -p /home/catkin_ws/src/
WORKDIR /home/catkin_ws
COPY . /home/catkin_ws/src/houseapi/

# Get msg dependencies
RUN git clone https://github.com/jariza/netatmo2ros.git ./src/netatmo2ros

# Compile ROS node
RUN /bin/bash -c " source /opt/ros/$ROS_DISTRO/setup.bash; /opt/ros/kinetic/bin/catkin_make"

# Default ROS master URI
ENV ROS_MASTER_URI=http://roscore-server:11311/

# Copy entrypoint file
COPY ros_entrypoint.sh /ros_entrypoint.sh
