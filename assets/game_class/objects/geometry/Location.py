import numpy as np
class Location():
    def __init__(self, x: np.float64=np.float64(0.) , y: np.float64=np.float64(0.), z: np.float64=np.float64(0.)):
        self.x = x
        self.y = y
        self.z = z