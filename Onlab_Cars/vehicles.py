# Take the all the vehicles most important attributes and place them in an explicit class:
class Vehicle:
    __slots__ = ["vehicle_id", "position", "road", "road_id"]

    def __init__(self, vehicle_id, position, road):
        self.vehicle_id = vehicle_id
        self.position = []
        self.position = position
        self.road = road
        # Magic so that it can be placed into a numpy array
        numbers = ""
        for letter in road:
            number = ord(letter) - 96
            numbers += str(abs(number))
        self.road_id = numbers

    def __str__(self):
        string = "ID: " + self.vehicle_id + " Geo: (" + str(round(self.position[0], 1)) + ", " + str(
            round(self.position[1], 1)) + ")"
        return string

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
            string += str(x)
        string += "\n"
        return string

    # FIXME only add a car if it is not present
    def addcar(self, car):
        for x in self.cars_on_this_road:
            if car.vehicle_id == x.vehicle_id:
                return
        self.cars_on_this_road.append(car)
        # print("Added ", car.vehicle_id, " to ", self.road_id)

    def checkcar(self):
        self.cars_on_this_road.clear()


class Map:
    __slots__ = ["size", "roads"]

    def __init__(self, road_list):
        self.roads = []
        for x in road_list:
            self.roads.append(Road(str(x)))
        self.size = len(self.roads)

    def flush(self):
        for road in self.roads:
            road.checkcar()

    def print(self):
        for x in self.roads:
            print(x)
