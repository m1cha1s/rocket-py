import math
from rocket import Rocket

class Atmosphere:
    def __init__(self) -> None:
        self.MzG = 6.67243 * 5.9722 * (10**13)
        self.Rz = 6371000

        self.p0 = 1013 * (10**2)
        self.R = 8.31446261815324
        self.u = 0.02896

        self.r = 287.05

    # g[m/s^2]
    def getGravity(self, rkt: Rocket) -> float:
        return self.MzG / ((self.Rz + rkt.pos[1])**2)

    # t[°K]
    def getTemperature(self, rkt: Rocket) -> float:
        return 288 * (1-(rkt.pos[1]/100000))

    # p[Pa]
    def getPressure(self, rkt: Rocket) -> float:
        return self.p0 * math.exp(-(self.u * self.getGravity(rkt) * rkt.pos[1]) / (self.R * self.getTemperature(rkt)))

    # d[kg/m^3]
    def getAirDensity(self, rkt: Rocket) -> float:
        return self.getPressure(rkt) / (self.r * self.getTemperature(rkt))