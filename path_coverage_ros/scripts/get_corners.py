#!/usr/bin/env python3
import rospy
from nav_msgs.msg import MapMetaData

def mapMetaDataCallBack(info):
    print("INFO:")
    print(info.origin.position)

def main():
    rospy.init_node('map_corners')
    rospy.Subscriber('map_metadata', MapMetaData, mapMetaDataCallBack);
    rospy.spin();


if __name__ == "__main__":
    main();

