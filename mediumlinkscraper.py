#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from xml.dom import minidom
requests.packages.urllib3.disable_warnings()
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
        os.system("clear")

print("    ___    __                   __  ___                   ")
print("   /   |  / /_  ____ ___  ___  / /_/   | __  ___________ _")
print("  / /| | / __ \/ __ `__ \/ _ \/ __/ /| |/ / / / ___/ __ `/")
print(" / ___ |/ / / / / / / / /  __/ /_/ ___ / /_/ / /  / /_/ / ")
print("/_/  |_/_/ /_/_/ /_/ /_/\___/\__/_/  |_\__,_/_/   \__,_/  ")
print("\nGithub : ahmetaura")
print("Twitter : rootaura\n")

dateinput = input("Please give time interval (ex: 2018-05-12 to 2019-02-23) : ")
splitinput = dateinput.split(" to ")

date1 = splitinput[0].split("-")
date2 = splitinput[1].split("-")

for year in range(int(date1[0]),int(date2[0])+1):
    for month in range(int(date1[1]),int(date2[1])+1):
        for day in range(int(date1[2]),int(date2[2])+1):
            stryear = str(year)
            strmonth = str(month)
            strday = str(day)
            if len(str(month)) == 1:
                strmonth = "0" + strmonth
            if len(str(day)) == 1:
                strday = "0" + strday
            strdate = stryear + "-" + strmonth + "-" + strday
            response = requests.get("https://medium.com/sitemap/posts/" + stryear + "/posts-" + strdate +  ".xml",verify=False)

            print("https://medium.com/sitemap/posts/" + stryear + "/posts-" + strdate +  ".xml")
