#!/usr/bin/env python

from __future__ import print_function

import sys
from os import path, getenv
import time


class hello:
    def __init__( self ):
        print("inside test.py")
        while 1 :
            time.sleep(3) 
            print("thread is running")
