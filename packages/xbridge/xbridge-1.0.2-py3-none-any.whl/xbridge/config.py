
import os

class UserInfo:
    pass


class Config:
    preferLocales = ['zh']

    def __init__(self, dir: str = None) -> None:
        # load config from dir
        # ...
        print('dir', dir)
        if dir:
            self.dir = dir
        else:
            # default_dir = 
            # global default_dir
            self.dir = os.path.join(os.environ['HOME'], '.xbridge')

    def getRSA():
        pass

    def getInfo() -> UserInfo:
        pass
    
