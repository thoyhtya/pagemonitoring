#!/usr/bin/python3
import json
import requests
from time import sleep
from datetime import datetime

def start_polling(url, interval, logfile):
    with open(logfile, "a") as f:
        response_time = requests.get(url).elapsed.total_seconds()
        logstring = "{} {} {}s".format(datetime.now(), url, response_time)
        print(logstring)
        f.write(logstring)

def main():
    #should probably read these from somewhere else
    log_path = "/opt/pagemonitor/pagemonitor.log"
    config_path = "/opt/pagemonitor/config.json"

    try:
        with open(config_path, encoding="UTF-8") as json_file:
            data = json.load(json_file)

        for site in data["urls"]:
            url = site["url"]
            interval = site["interval"]
            start_polling(url, interval, log_path)

    except ValueError as e:
        print("Error reading {} Check json syntax".format(config_path))
        raise

    # with open(log_path, "a") as logfile:
    #   logfile.write(data)


if __name__ == "__main__":
    main()
