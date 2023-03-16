# -*- coding: utf-8 -*-
import os, sys
import time

filename = "pioneer_MRT_area"

command_1 = "netconvert --osm-files {}.osm -o {}.net.xml".format(filename, filename)

command_2 = "polyconvert --net-file {}.net.xml --osm-files {}.osm --type-file osmPolyconvert.typ.xml -o {}.poly.xml".format(filename, filename, filename)

command_3 = "randomTrips.py --vehicle-class bus --trip-attributes='maxSpeed=\'27.8\'' -n {}.net.xml -r {}.rou.xml -e 100 -l".format(filename, filename)

os.popen(command_1)
time.sleep(0.5)
os.popen(command_2)
time.sleep(0.5)
os.popen(command_3)
time.sleep(0.5)
sumocfg = """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
 <input>
  <net-file value="%s.net.xml"/>
  <route-files value="%s.rou.xml"/>
  <additional-files value="%s.poly.xml"/>
 </input>
 <time>
  <begin value="0"/>
  <end value="10000"/>
  <step-length value="0.1"/>
 </time>
</configuration>""" % (filename, filename, filename)

f = open("{}.sumocfg".format(filename), "w")
f.write(sumocfg)
f.close()

print("Done")

# Finally, run the following in the command prompt

# cd C:\Users\ethan.png\Documents\pioneermrt

# sumo-web3d -c C:/Users/ethan.png/Documents/pioneermrt/pioneer.sumocfg

