import numpy as np
from rocket import Rocket

class Engine:
    def __init__(self, exhaustVel: float, fuelMass: float, fuelUsage: float) -> None:
        self.exhaustVel: float = exhaustVel
        self.fuelMass: float = fuelMass
        self.fuelUsage: float = fuelUsage

    def applyForce(self, rkt: Rocket):
        if self.fuelMass > 0:
            rkt.applyForce(np.array((0, self.exhaustVel * self.fuelUsage)))

    def useFuel(self, dt: float):
        if self.fuelMass > 0:
            self.fuelMass -= self.fuelUsage * dt

if __name__ == "__main__":
    pass