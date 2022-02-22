import numpy as np
from rocket import Rocket

class AirDrag:
    def __init__(self, fluidDensity: float, area: float, dragCoefficient: float) -> None:
        self.fluidDensity: float = fluidDensity
        self.area: float = area
        self.dragCoefficient: float = dragCoefficient

    def applyDrag(self, rkt: Rocket):
        v = np.linalg.norm(rkt.vel)
        drag = 0.5 * self.fluidDensity * v * v * self.dragCoefficient * self.area

        
