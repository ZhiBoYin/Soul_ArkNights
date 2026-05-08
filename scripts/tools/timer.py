import time
from scripts.logger.Log import Log
def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        Log.log(f"time consumption of {func.__name__}: {(end_time - start_time):.4f}")
        return res
    return warpper