#!/usr/bin/env python
# coding=utf-8
"""
    House REST API
    Author: José Jaime Ariza (jariza@ieee.org).
    Python version: 2.7
"""

from flask import Flask, jsonify
import rospy
from rospy_message_converter import message_converter
import thread
from netatmo2ros.msg import WeatherdataArray


app = Flask(__name__)

# Weather data
weather_status = ""


@app.route("/weather")
def weather():
    """
    Function triggered by /weather path
    :return: JSON data with the content of the weather ROS topic
    """
    global weather_status
    if weather_status != "":
        d_weather_status = message_converter.convert_ros_message_to_dictionary(weather_status)
    else:
        d_weather_status = dict()
    return jsonify(d_weather_status)


def callback_weather(data):
    """
    Callback for receiving data from /weather ROS topic
    :param data: Data from /weather ROS topic
    """
    global weather_status
    weather_status = data


def listener():
    """
    Launchs the ROS topics listener
    """
    rospy.init_node("houseapi", anonymous=True, disable_signals=True)
    rospy.Subscriber("weather", WeatherdataArray, callback_weather)


if __name__ == '__main__':
    thread.start_new_thread(listener, tuple())
    # I know, I know: this is bad and should never reach production or real environments...
    app.run(debug=False, host="0.0.0.0")

