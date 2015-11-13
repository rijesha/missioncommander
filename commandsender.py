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
    def __init__(self, verbose=False):
        self.verbose = verbose
        self._interface = IvyMessagesInterface(self.message_recv)

    def message_recv(self, ac_id, msg):
        if self.verbose:
            print("Got msg %s" % msg.name)

    def shutdown(self):
        print("Shutting down ivy interface...")
        self._interface.shutdown()

    def __del__(self):
        self.shutdown()

    def add_mission_command(self, msg_id="", ac_id = "5", insert = "APPEND" , wp_lat="", wp_lon="", wp_alt="", duration = "60", center_lat="", center_lon="", center_alt="", radius="60",segment_lat_1="", segment_lat_2="", segment_lon_1="", segment_lon_2="", segment_alt="", point_lat_1="", point_lon_1="", point_lat_2="", point_lon_2="", point_lat_3="", point_lon_3="", point_lat_4="", point_lon_4="", point_lat_5="", point_lon_5="", path_alt, nb="", survey_lat_1="", survey_lon_1="", survey_lat_2="", survey_lon_2="", survey_alt=""):
        msg = PprzMessage("datalink", msg_id)
        msg['id'] = ac_id
        msg['insert'] = insert
        msg['wp_lat'] = wp_lat	
        msg['wp_lon'] = wp_lon
        msg['wp_alt'] = wp_alt
        msg['duration'] = duration

        msg['center_lat'] = center_lat
        msg['center_lon'] = center_lon
        msg['center_alt'] = center_alt
        msg['radius'] = radius

        msg['segment_lat_1'] = segment_lat_1
        msg['segment_lon_1'] = segment_lon_1
        msg['segment_lat_2'] = segment_lat_2
        msg['segment_lon_2'] = segment_lon_2

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

        msg['survey_lat_1'] = survey_lat_1
        msg['survey_lon_1'] = survey_lon_1
        msg['survey_lat_2'] = survey_lat_2
        msg['survey_lon_2'] = survey_lon_2

        msg['survey_alt'] = survey_alt

        print("Sending message: %s" % msg)
        self._interface.send(msg)


if __name__ == '__main__':
    cs = CommandSender()
    cs.add_mission_command(obstacle_id=1, color="ff0000", status=1, lat=434624607, lon=12723454, radius=100, alt=1720000)
    cs.shutdown()


