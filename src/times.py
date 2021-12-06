#!/usr/bin/env python

import numpy as np
from datetime import datetime
import time


def CreateDateTimeFromInput(hour, minutes):
    try:
        # create a datetime object from the input hour and minutes
        now = datetime.now()
        dateTime = datetime(now.year, now.month, now.day, hour, minutes)
        return dateTime
    except Exception as e:
        print(f'{e} ❌')


def ReadDateTimeObjects(file):
    # read the hour and minutes from the file
    try:
        # read the file and create a list of datetime objects
        with open(file, 'r+') as f:
            lines = f.readlines()
            dateTimeList = []
            for line in lines:
                hour, minutes = line.split(':')
                dateTime = CreateDateTimeFromInput(int(hour), int(minutes))
                dateTimeList.append(dateTime)
            return dateTimeList
    except Exception as e:
        print(f'{e} ❌')


def GetUNIXTimestamp(timestamp_obj):
    # get UNIX timestamp from a datetime object
    try:
        timestamp = time.mktime(timestamp_obj.timetuple())
        return timestamp
    except Exception as e:
        print(f'{e} ❌')


def Execute_Main_Procedure():
    # execute the main procedure
    time_list = ReadDateTimeObjects('hours.txt')
    print('evaluating time elements')
    for time in time_list:
        hour = now.hour
        minutes = now.minute
        print(GetUNIXTimestamp(time))
    #get current tiem in epoch
    print(GetUNIXTimestamp(now))


if __name__ == '__main__':
    try:
        # get current time as a timestamp for the initial script execution
        now = datetime.utcnow()
        print(f'{now} - Starting times.py ✅')

        # execute the main procedure of the codebase
        Execute_Main_Procedure()

    except Exception as e:
        print(f'{e} ❌')
