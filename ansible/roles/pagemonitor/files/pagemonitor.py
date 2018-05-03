#!/usr/bin/python3
import json
import requests
from time import sleep
from datetime import datetime
from multiprocessing import Process

#makes request to specified url 
#repeats after interval in seconds
#logs results to a file
def polling_process(url, interval, logfile):
    while True:
        with open(logfile, "a") as f:
            #example log line
            #timestamp url elapsed_time
            #2018-05-03 16:24:57.241970 http://www.kaleva.fi/ 0.294813s

            response_time = requests.get(url).elapsed.total_seconds()
            logstring = "{} {} {}s\n".format(datetime.now(), url, response_time)
            # print(logstring)
            f.write(logstring)
        sleep(interval)

#reads config.json and spawns polling process for each site specified
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

            p = Process(target=polling_process, args=(url, interval, log_path))
            p.start()

    except ValueError as e:
        print("Error reading {} Check json syntax".format(config_path))
        raise

if __name__ == "__main__":
    main()
