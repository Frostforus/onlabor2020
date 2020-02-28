import sys
import os
import traci
from vehicles import *
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from collections import Counter
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))
traci.start(["sumo-gui", "-c", "test.sumocfg"])

city = Map(traci.edge.getIDList())
# TODO at kell irni


step = 0
while step < 170:
    traci.simulationStep()
    step += 1
    print("\n\nNew step:", step)

    # TODO: Stuff here
    # update road database:
    # flush cars no longer on roads:
    city.flush(traci.vehicle.getIDList())

    # add vehicles to road:
    for veh_id in traci.vehicle.getIDList():
        this_road = traci.vehicle.getRoadID(veh_id)
        for road in city.roads:
            if road.road_id == this_road:
                road.addcar(Vehicle(veh_id, [0, 0], road))

    #TODO try printing the cars on the roads: for DBSCAN
    # Get the vehicles and their positions for each road seperatly, and run DBSCAN on it
    city.print()


traci.close(True)
