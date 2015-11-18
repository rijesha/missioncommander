#!/usr/bin/env python

from __future__ import print_function

import sys
from os import path, getenv

# if PAPARAZZI_SRC not set, then assume the tree containing this
# file is a reasonable substitute
PPRZ_SRC = getenv("PAPARAZZI_SRC", path.normpath(path.join(path.dirname(path.abspath(__file__)), '../../../../')))
sys.path.append(PPRZ_SRC + "/sw/lib/python")

from ivy_msg_interface import IvyMessagesInterface
from pprz_msg.message import PprzMessage

class CommandSender(object):
    def __init__(self, verbose=False, callback = None):
        self.verbose = verbose
        self.callback = callback
        self._interface = IvyMessagesInterface(self.message_recv)

    def message_recv(self, ac_id, msg):
        if (self.verbose and self.callback != None):
            self.callback(ac_id, msg)

    def shutdown(self):
        print("Shutting down ivy interface...")
        self._interface.shutdown()

    def __del__(self):
        self.shutdown()

    def add_mission_command(self, msg_id = "", ac_id = 5 , insert = "APPEND" , wp_lat = "", wp_lon = "", wp_alt = "", duration = "60", center_lat = "", center_lon = "", center_alt = "", radius = "60",segment_lat_1 = "", segment_lat_2 = "", segment_lon_1 = "", segment_lon_2 = "", segment_alt = "", point_lat_1 = "", point_lon_1 = "", point_lat_2 = "", point_lon_2 = "", point_lat_3 = "", point_lon_3 = "", point_lat_4 = "", point_lon_4 = "", point_lat_5 = "", point_lon_5 = "", path_alt = "", nb = "", survey_lat_1 = "", survey_lon_1 = "", survey_lat_2 = "", survey_lon_2 = "", survey_alt = ""):
        msg = PprzMessage("datalink", msg_id)
        msg['ac_id'] = ac_id
        msg['insert'] = insert
        msg['wp_lat'] = wp_lat	
        msg['wp_lon'] = wp_lon
        msg['wp_alt'] = wp_alt
        msg['duration'] = duration



        print("Sending message: %s" % msg)
        self._interface.send(msg)

    def add_obstacle(self, obstacle_id, color, status, lat, lon, radius, alt):
        msg = PprzMessage("ground", "OBSTACLE")
        msg['id'] = obstacle_id
        msg['color'] = color
        msg['status'] = status
        msg['lat'] = lat
        msg['lon'] = lon
        msg['radius'] = radius
        msg['alt'] = alt
        print("Sending message: %s" % msg)
        self._interface.send(msg)

# add_mission_command(msg_id = "MISSION_GOTO_WP_LLA", ac_id=5, insert = "0", wp_lat=434624607, wp_lon=12723454, wp_alt=700, duration =60)



