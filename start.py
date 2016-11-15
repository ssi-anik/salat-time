#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import dotenv module
import dotenv
# import datetime
from datetime import datetime

# load the env file
dotenv.load('./.env')

# alias the dotenv.get
get = dotenv.get

#get the time format
format = get('TIME_FORMAT')

if format not in [12, 24]:
	raise Exception('Time format should either be 12 or 24')

def format_time(utime):
	if "am" in utime.lower() or "pm" in utime.lower():
		return utime[:-3]

# get the fajr prayer time
fajr = get('FAJR')
formatted_fajr = format_time(fajr) if format == 12 else fajr

# get the zuhr prayer time
zuhr = get('ZUHR')
formatted_zuhr = format_time(zuhr) if format == 12 else zuhr

# get the asr prayer time
asr = get('ASR')
formatted_asr = format_time(asr) if format == 12 else asr

# get the magrib prayer time
magrib = get('MAGRIB')
formatted_magrib = format_time(magrib) if format == 12 else magrib

# get the isha prayer time
isha = get('ISHA')
formatted_isha = format_time(isha) if format == 12 else isha

# current time
dt = datetime.now()

print("{} {} {} {} {}".format(fajr, zuhr, asr, magrib, isha))