import pprint


class Auto:
    def __init__(self, v, distance, color, max_speed, fuel_supply, cost):
        self.v = v
        self.distance = distance
        self.color = color
        self.max_speed = max_speed
        self.fuel_supply = fuel_supply
        self.cost = cost

    def __lt__(self, other):
        if self.cost == other.cost:
            if self.v == other.v:
                if self.fuel_supply == other.fuel_supply:
                    return False
                elif self.fuel_supply < other.fuel_supply:
                    return True
            elif self.v < other.v:
                return True
        if self.cost < other.cost:
            return True

    def __repr__(self):
        return "Car(cost={}, v={}, fuel_supply={}, distance={}, color={}, max_speed={})".format(
            self.cost, self.v, self.fuel_supply, self.distance, self.color, self.max_speed)


cars = [Auto(3, 10000, 'white', 150, 60, 4000), Auto(2, 15000, 'yellow', 150, 50, 3000),
        Auto(1, 20000, 'black', 150, 70, 4200), Auto(3, 17500, 'purple', 150, 50, 3100),
        Auto(2, 52000, 'green', 150, 40, 5000), Auto(1, 30000, 'orange', 150, 30, 5000),
        Auto(2, 40000, 'white', 150, 90, 5000), Auto(3, 50000, 'green', 150, 80, 5000),
        Auto(1, 60000, 'purple', 150, 40, 2300)
        ]

pprint.pprint(sorted(cars))
