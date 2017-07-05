import config
import requests
import json
import time
import os
import csv


def make_request(location):
	if location == "outdoor":
		return "https://api.darksky.net/forecast/{0}/{1},{2}".format(config.key, config.gps_coords[0], config.gps_coords[1])
	if location == "indoor":
		return "http://{0}/weather".format(config.esp_ip)


def write_to_file(date, time, weather):
	with open('temp_data/' + date + '.csv', 'a', newline='') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',')
		csv_writer.writerow([time, weather[0], weather[1], weather[2], weather[3]])


if __name__ == "__main__":

	# outdoor_weather = requests.get(make_request("outdoor")).json()

	# print("Outdoor temperature:")
	# print(outdoor_weather["currently"]["temperature"])

	# print("Outdoor humidity:")
	# print(outdoor_weather["currently"]["humidity"])

	# indoor_weather = requests.get(make_request("indoor")).json()

	# print("Indoor temperature:")
	# print(indoor_weather["temperature"])

	# print("Indoor humidity:")
	# print(indoor_weather["humidity"])

	current_time = time.localtime()

	# year = time.strftime("%Y", current_time)
	# month = time.strftime("%b", current_time)
	# weekday = time.strftime("%a", current_time)
	# day = time.strftime("%d", current_time)
	# hour = time.strftime("%H", current_time)
	# minute = time.strftime("%M", current_time)
	# print("{0}:{1}:00 {2}, {3} {4} {5}".format(hour, minute, weekday, month, day, year))

	date = time.strftime("%m_%d_%Y", current_time)
	time = time.strftime("%H:%M")
	weather = [77,54,82,49]

	print(date)
	print(time)
	print(weather)

	write_to_file(date, time, weather)
