from atmosphere import Atmosphere
import numpy as np
from rocket import Rocket
from sklearn.preprocessing import normalize

class AirDrag:
    def __init__(self, area: float, dragCoefficient: float) -> None:
        self.area: float = area
        self.dragCoefficient: float = dragCoefficient

    # drag[N]
    def applyDrag(self, rkt: Rocket, atm: Atmosphere):
        v = np.linalg.norm(rkt.vel)
        drag = 0.5 * atm.getAirDensity(rkt) * v * v * self.dragCoefficient * self.area
        dragForce = normalize(rkt.vel[:,np.newaxis], axis=0).ravel() * -1.0 * drag

        rkt.applyForce(dragForce)