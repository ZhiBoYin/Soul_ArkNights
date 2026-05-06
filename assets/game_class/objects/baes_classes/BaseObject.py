from assets.game_class.objects.geometry.Location import Location
from typing import Optional,Generator
class BaseObject():
    
    @staticmethod
    def gen_unicode() -> Generator[str,None,None]:
        number = 0
        while True:
            yield f"{number:.12d}"
            number += 1
    unicode_generator = gen_unicode()

    """
    object_unique_code is the unique string to represent this object
    object_id is the id of this object, it is designed to be the same for the same 'leaf class'
    location is the location of this object
    """
    def __init__(self, object_unicode: str, object_id: str, location: Optional[Location]=None):
        self._object_unicode:str = next(BaseObject.unicode_generator)
        self.object_id = object_id
        self.location:Location = Location() if location is None else location
        

    def __eq__(self,o):
        if not isinstance(o,BaseObject):
            raise TypeError(f"{type(o)} can not compare with {type(self)}")
        return self._object_unicode==o.get_object_unicode()
    
    def __hash__(self):
        return hash(self._object_unicode)
    
    def get_object_unicode(self):
        return self._object_unicode
