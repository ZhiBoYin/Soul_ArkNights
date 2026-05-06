from assets.game_class.objects.baes_classes.BaseObject import BaseObject
from assets.game_class.objects.geometry.Location import Location
import numpy as np
from typing import Optional
class TouchableObject(BaseObject):
    """
    location 
    """
    def __init__(self,object_unicode: str, object_id: str,\
                x_width: np.float64, y_width: np.float64, z_width: np.float64,\
                location: Optional[Location]=None,\
                collisionBox: Optional[Box]= None):
        self.x_width = x_width
        self.y_width = y_width
        self.z_width = z_width
        self.CollisionBox = RectangularBox if collisionBox is None else collisionBox
    def CollisionBox(self):
        return 
        
"""
should also implement a way for decide whether a object is touch,overlap, or disjoint with:
    a. another object
    b. a line,plane or space(3d)/object
"""