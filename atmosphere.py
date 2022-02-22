import math
from rocket import Rocket

class Atmosphere:
    def __init__(self) -> None:
        self.MzG = 6.67 * 5.9722 * (10**13)
        self.Rz = 6371000

        self.p0 = 1013 * (10**2)
        self.R = 8.31446261815324
        self.u = 0.02896

        self.r = 287.05

    def getGravity(self, rkt: Rocket) -> float:
        return self.MzG / ((self.Rz + rkt.pos[1])**2)

    def getTemperature(self, rkt: Rocket) -> float:
        return 288 * ((-rkt.pos[1]/100000) + 1)

    def getPressure(self, rkt: Rocket) -> float:
        return self.p0 * math.exp(-(self.u * self.getGravity(rkt.pos[1]) * rkt.pos[1]) / (self.R * self.getTemperature(rkt.pos[1])))

    def getAirDensity(self, rkt: Rocket) -> float:
        return self.getPressure(rkt.pos[1]) / (self.r * self.getTemperature(rkt.pos[1]))