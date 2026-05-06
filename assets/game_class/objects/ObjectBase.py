import abc
class Object(abc.ABC):
    def __init__(self,obj_ID:str):
        self._object_ID:str = obj_ID

    def __eq__(self,o):
        if not isinstance(o,Object):
            raise TypeError(f"{type(o)} can not compare with {type(self)}")
        return self._object_ID==o.get_object_ID()
    def __hash__(self):
        return hash(self._object_ID)
    
    def get_object_ID(self):
        return self._object_ID
