import numpy as np

class Rocket:
    def __init__(self, pos: np.ndarray, vel: np.ndarray, acc: np.ndarray, mass: float) -> None:
        self.pos: np.ndarray = pos
        self.vel: np.ndarray = vel
        self.acc: np.ndarray = acc

        self.rocketMass: float = mass

        self.mass: float = mass

    def setTotalMass(self, engineMass: float):
        self.mass = self.rocketMass + engineMass

    def applyForce(self, force: np.ndarray):
        self.acc += force / self.mass

    def applyGravity(self, g: float):
        self.acc[1] -= g

    def update(self, dt: float):
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        self.acc *= 0


if __name__ == "__main__":
    pass