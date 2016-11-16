#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from datetime import datetime
import subprocess
import os

if time_format not in [12, 24]:
	raise Exception('Time format should either be 12 or 24')

def get_current_time():
	now = datetime.now()
	return "{}:{}".format(now.hour, now.minute)

def format_time(utime):
	if "am" in utime.lower():
		return utime[:-2]
	elif "pm" in utime.lower():
		utime = utime.lower().replace('pm', '')
		splited = utime.split(':')
		new_time = 12 + int(splited[0])
		return "{}:{}".format(new_time, splited[1])

def is_notifiable_difference(from_time, to_time):
	global notify_before
	format = "%H:%M"
	t1 = datetime.strptime(from_time, format)
	t2 = datetime.strptime(to_time, format)
	return True if (((t1 - t2).seconds) // 60) == notify_before else False

def send_notification(summary = "Salat time", body = "It's salat time"):
	subprocess.call(['notify-send', '-u', 'critical', '-i', os.path.abspath('./icons/salat_time-48.png'), summary, body])
	global enable_tone
	if enable_tone.lower() != "false":
		subprocess.call(['paplay', os.path.abspath('./sounds/alert.wav')])

# get the fajr prayer time
fajr = fajr.strip()
formatted_fajr = format_time(fajr) if time_format == 12 else fajr

# get the zuhr prayer time
zuhr = zuhr.strip()
formatted_zuhr = format_time(zuhr) if time_format == 12 else zuhr

# get the asr prayer time
asr = asr.strip()
formatted_asr = format_time(asr) if time_format == 12 else asr

# get the magrib prayer time
magrib = magrib.strip()
formatted_magrib = format_time(magrib) if time_format == 12 else magrib

# get the isha prayer time
isha = isha.strip()
formatted_isha = format_time(isha) if time_format == 12 else isha

# current time
now = get_current_time()

if is_notifiable_difference(formatted_fajr, now):
	send_notification(body = "It's Fajr prayer time")
elif is_notifiable_difference(formatted_zuhr, now):
	send_notification(body = "It's Zuhr prayer time")
elif is_notifiable_difference(formatted_asr, now):
	send_notification(body = "It's Asr prayer time")
elif is_notifiable_difference(formatted_magrib, now):
	send_notification(body = "It's Magrib prayer time")
elif is_notifiable_difference(formatted_isha, now):
	send_notification(body = "It's Isha prayer time")
