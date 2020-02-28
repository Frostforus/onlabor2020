# Take the all the vehicles most important attributes and place them in an explicit class:
class Vehicle:
    __slots__ = ["vehicle_id", "position", "road"]

    def __init__(self, vehicle_id, position, road):
        self.vehicle_id = vehicle_id
        self.position = position
        self.road = road

    def __str__(self):
        return self.vehicle_id

    # TODO


class Road:
    __slots__ = ["road_id", "cars_on_this_road"]

    def __init__(self, road_id):
        self.road_id = road_id
        self.cars_on_this_road = []

    def __str__(self):
        string = self.road_id + ": "
        for x in self.cars_on_this_road:
            string += " "
            string += x.vehicle_id
        return string

    # FIXME only add a car if it is not present
    def addcar(self, car):
        for x in self.cars_on_this_road:
            if car.vehicle_id == x.vehicle_id:
                return
        self.cars_on_this_road.append(car)
        # print("Added ", car.vehicle_id, " to ", self.road_id)

    def checkcar(self, car):
        for x in self.cars_on_this_road:
            if car == x.vehicle_id:
                self.cars_on_this_road.remove(x)
                # print("Removed ", car, " from ", self.road_id)
                return


class Map:
    __slots__ = ["size", "roads"]

    def __init__(self, road_list):
        self.roads = []
        for x in road_list:
            self.roads.append(Road(str(x)))
        self.size = len(self.roads)

    def flush(self, car_list):
        for road in self.roads:
            for car in car_list:
                road.checkcar(car)

    def print(self):
        for x in self.roads:
            print(x)
