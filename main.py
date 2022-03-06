import numpy as np
import matplotlib.pyplot as plt

from rocket import Rocket
from airDrag import AirDrag
from engine import Engine
from atmosphere import Atmosphere

def main():
    atm = Atmosphere()
    
    ad = AirDrag(np.pi, 0.45)
    
    eng = Engine(90, 10, 100000, 0.7)

    rkt = Rocket(
        np.array((0, 0.1)), 
        np.zeros(2),
        np.zeros(2),
        10
    )

    data = {
        'time': [],
        'g': [],
        'mass': [],
        'pos': {
            'x': [],
            'y': []
        },
        'vel': {
            'x': [],
            'y': []
        },
        'acc': {
            'x': [],
            'y': []
        }        
    }

    dt = 0.01
    time = 0


    while rkt.pos[1] > 0:
        g = atm.getGravity(rkt)

        eng.applyForce(rkt)
        ad.applyDrag(rkt, atm)

        eng.useFuel(dt)
        rkt.setTotalMass(eng.fuelMass)

        rkt.applyGravity(g)
        
        data['pos']['x'].append(rkt.pos[0])
        data['pos']['y'].append(rkt.pos[1])

        data['vel']['x'].append(rkt.vel[0])
        data['vel']['y'].append(rkt.vel[1])
        
        data['acc']['x'].append(rkt.acc[0])
        data['acc']['y'].append(rkt.acc[1])
        
        data['time'].append(time)

        data['g'].append(g)

        data['mass'].append(rkt.mass)

        rkt.update(dt)

        
        # print(rkt.pos, rkt.vel, rkt.acc, g, time)

        time += dt

    # print(data)
    plt.plot(data['time'], data['pos']['y'])
    plt.plot(data['time'], data['vel']['y'])
    plt.plot(data['time'], data['acc']['y'])
    plt.plot(data['time'], data['mass'])

    plt.legend(["pos.x", "vel.y", "acc.y", "mass"])
    plt.show()

if __name__ == "__main__" :
    main()