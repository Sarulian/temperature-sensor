import config
import requests
import json
import time
import os
import csv


def make_outdoor_request():
	return "https://api.darksky.net/forecast/{0}/{1},{2}".format(config.key, config.gps_coords[0], config.gps_coords[1])


def make_indoor_request(value):
	return "http://{0}/{1}".format(config.esp_ip, value)


def clean_temp(temp_str):
	return int(temp_str[13:15])


def clean_humidity(humidity_str):
	return int(humidity_str[10:12])/100


def write_to_file(date, time, weather):
	path = config.data_path + date + '.csv'
	print(path)
	with open(path, 'a', newline='') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',')
		csv_writer.writerow([time, weather[0], weather[1], weather[2], weather[3]])


if __name__ == "__main__":

	outdoor_weather = requests.get(make_outdoor_request()).json()

	indoor_temp_str = requests.get(make_indoor_request("temp")).text
	indoor_humidity_str = requests.get(make_indoor_request("humidity")).text

	current_time = time.localtime()

	date = time.strftime("%m_%d_%Y", current_time)
	time = time.strftime("%H:%M")
	weather = [outdoor_weather["currently"]["temperature"],outdoor_weather["currently"]["humidity"],
				clean_temp(indoor_temp_str),clean_humidity(indoor_humidity_str)]

	print(date)
	print(time)
	print(weather)

	write_to_file(date, time, weather)

	print("Done!")
