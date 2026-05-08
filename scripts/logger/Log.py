import time

class Log:
    
    logType_to_path = {"RunTime":"logs/runtime_log.txt",
                       "Map":"logs/map_log/log,txt",
                       "Player":"logs/player_log/log.txt"}
    @staticmethod
    def log(content:str ,logType: str = "RunTime") -> None:
        if logType not in Log.logType_to_path.keys():
            raise ValueError("log type should be one of {logType_to_path.keys()}")
        
        with open(Log.logType_to_path[logType],'a',encoding='utf-8') as f:
            f.write(f"{time.ctime} : {content}")