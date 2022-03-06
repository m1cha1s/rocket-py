from math import sqrt
import numpy as np
from rocket import Rocket

class Engine:
    def __init__(self, fuelMass: float, fuelUsage: float, fuelEnergy: float, efficiency: float) -> None:
        self.fuelMass: float = fuelMass
        self.fuelUsage: float = fuelUsage

        self.fuelEnergy = fuelEnergy
        self.efficiency = efficiency

    def applyForce(self, rkt: Rocket):
        if self.fuelMass > 0:
            force = np.array((0, sqrt(2* self.fuelEnergy * self.efficiency) * self.fuelUsage))
            # print(force)
            rkt.applyForce(force)
            # print(rkt.acc)

    def useFuel(self, dt: float):
        if self.fuelMass > 0:
            self.fuelMass -= self.fuelUsage * dt

if __name__ == "__main__":
    pass