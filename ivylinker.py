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
        msg['duration'] = duration
	
        if msg_id == MISSION_GOTO_WP_LLA:
            msg['wp_lat'] = wp_lat	
            msg['wp_lon'] = wp_lon
            msg['wp_alt'] = wp_alt

        elif msg_id == MISSION_CIRCLE_LLA:
            msg['center_lat'] = center_lat
            msg['center_lon'] = center_lon
            msg['center_alt'] = center_alt
            msg['radius'] = radius

        elif msg_id == MISSION_SEGMENT_LLA:
            msg['segment_lat_1'] = segment_lat_1
            msg['segment_lon_1'] = segment_lon_1
            msg['segment_lat_2'] = segment_lat_2
            msg['segment_lon_2'] = segment_lon_2

        elif msg_id == MISSION_PATH_LLA:
            msg['point_lat_1'] = point_lat_1
            msg['point_lon_1'] = point_lon_1
            msg['point_lat_2'] = point_lat_2
            msg['point_lon_2'] = point_lon_2
            msg['point_lat_3'] = point_lat_3
            msg['point_lon_3'] = point_lon_3
            msg['point_lat_4'] = point_lat_4
            msg['point_lon_4'] = point_lon_4
            msg['point_lat_5'] = point_lat_5
            msg['point_lon_5'] = point_lon_5
            msg['path_alt'] = path_alt
            msg['nb'] = nb

        elif msg_id == MISSION_SURVEY_LLA:
            msg['survey_lat_1'] = survey_lat_1
            msg['survey_lon_1'] = survey_lon_1
            msg['survey_lat_2'] = survey_lat_2
            msg['survey_lon_2'] = survey_lon_2
            msg['survey_alt'] = survey_alt


        print("Sending message: %s" % msg)
        self._interface.send(msg)

    def add_mission_command_dict(self, ac_id, insert, msg_id, msgs):
        print('hello')
        msg = PprzMessage("datalink", msg_id)
	
        print(msgs)
        print(msgs.keys)
        print(msgs.get('duration'))
        msg['ac_id'] = ac_id
        msg['insert'] = insert
        msg['duration'] = msgs.get('duration')
	
        if msg_id == 'MISSION_GOTO_WP_LLA':
            msg['wp_lat'] = msgs.get('wp_lat')
            msg['wp_lon'] = msgs.get('wp_lon')
            msg['wp_alt'] = msgs.get('wp_alt')

        elif msg_id == 'MISSION_CIRCLE_LLA':
            msg['center_lat'] = msgs.get('center_lat')
            msg['center_lon'] = msgs.get('center_lon')
            msg['center_alt'] = msgs.get('center_alt')
            msg['radius'] = msgs.get('radius')

        elif msg_id == 'MISSION_SEGMENT_LLA':
            msg['segment_lat_1'] = msgs.get('segment_lat_1')
            msg['segment_lon_1'] = msgs.get('segment_lon_1')
            msg['segment_lat_2'] = msgs.get('segment_lat_2')
            msg['segment_lon_2'] = msgs.get('segment_lon_2')

        elif msg_id == 'MISSION_PATH_LLA':
            msg['point_lat_1'] = msgs.get('point_lat_1')
            msg['point_lon_1'] = msgs.get('point_lon_1')
            msg['point_lat_2'] = msgs.get('point_lat_2')
            msg['point_lon_2'] = msgs.get('point_lon_2')
            msg['point_lat_3'] = msgs.get('point_lat_3')
            msg['point_lon_3'] = msgs.get('point_lon_3')
            msg['point_lat_4'] = msgs.get('point_lat_4')
            msg['point_lon_4'] = msgs.get('point_lon_4')
            msg['point_lat_5'] = msgs.get('point_lat_5')
            msg['point_lon_5'] = msgs.get('point_lon_5')
            msg['path_alt'] = msgs.get('path_alt')
            msg['nb'] = msgs.get('nb')

        elif msg_id == 'MISSION_SURVEY_LLA':
            msg['survey_lat_1'] = msgs.get('survey_lat_1')
            msg['survey_lon_1'] = msgs.get('survey_lon_1')
            msg['survey_lat_2'] = msgs.get('survey_lat_2')
            msg['survey_lon_2'] = msgs.get('survey_lon_2')
            msg['survey_alt'] = msgs.get('survey_alt')


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



