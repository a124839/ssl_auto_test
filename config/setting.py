#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'litr'


import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# drivers path
DRIVER_PATH = os.path.join(BASE_DIR,"drivers")

FIREFOX_PATH = os.path.join(DRIVER_PATH,"geckodriver.exe")
CHROME_PATH = os.path.join(DRIVER_PATH,"chromedriver.exe")
EDGE_PATH = os.path.join(DRIVER_PATH,"msedgedriver.exe")

#logs path
LOG_PATH = os.path.join(BASE_DIR,"logs")

# report path
REPORT_PATH = os.path.join(BASE_DIR,"reports")

# resources path
RESOURCE_PATH = os.path.join(BASE_DIR,"resource")

IMAGE_PATH = os.path.join(BASE_DIR,"screenshot")


if __name__ == '__main__':
    print(DRIVER_PATH)
    print(LOG_PATH)
    print(REPORT_PATH)
    print(RESOURCE_PATH)



