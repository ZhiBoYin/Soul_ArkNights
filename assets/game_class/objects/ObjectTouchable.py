from assets.game_class.objects.BaseObject import BaseObject
from assets.game_class.objects.Location import Location
import numpy as np
class TouchableObject(BaseObject):
    def __init__(self,object_unicode: str, object_id: str,\
                width: np.float64, length: np.float64, height: np.float64,\
                location: Location=Location()):
        pass
        
"""
should also implement a way for decide whether a object is touch,overlap, or disjoint with:
    a. another object
    b. a line,plane or space(3d)/object
"""