import json
from typing import Dict

class UndeliverableError(LookupError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class baseObject:
    @property
    def __json__(self):
        data = {}
        for key in self.__dict__:
            if "__" not in key:
                if hasattr(self.__getattribute__(key), '__json__'):
                    data[key] = self.__getattribute__(key).__json__
                    continue
                try:
                    json.dumps({"data": self.__getattribute__(key)})
                    data[key] = self.__getattribute__(key)
                    continue
                except:
                    pass
                if type(self.__getattribute__(key)) == dict:
                    data[key] = {}
                    try:
                        dt = self.__getattribute__(key)
                        for i in dt:
                            if hasattr(dt[i], '__json__'):
                                data[key][i] = dt[i].__json__
                    except:
                        pass
                    continue
                if type(self.__getattribute__(key)) == list:
                    data[key] = []
                    try:
                        dt = self.__getattribute__(key)
                        for i in dt:
                            if hasattr(dt[i], '__json__'):
                                data[key].append(dt[i].__json__)
                        data[key] = dt
                    except:
                        pass
        return data

    def __loadJson__(self, js):
        for item in js:
            if item in self.__dict__:
                if hasattr(self.__getattribute__(item), '__loadJson__'):
                    self.__getattribute__(item).__loadJson__(js[item])
                else:
                    self.__setattr__(item, js[item])
        return self

class __requests__(baseObject):
    def __init__(self):
        self.maxPending = 0
        self.maxTime = 30

class __clientConfig__(baseObject):
    def __init__(self):
        self.requests = __requests__()

class __function__(baseObject):
    def __init__(self, function, maxPending, maxTime):
        self.maxPending:int = maxPending
        self.maxTime:int = maxTime
        self.__function__ = function
        self.function:str = function.__name__

class Variables(baseObject):
    pass

class clients:
    json    = 0
    python  = 1

class serviceInfo(baseObject):
    def __init__(self):
        self.name       = None
        self.version    = None
        self.include    = None
        self.id         = None
        self.client     = clients.json
        self.config     = __clientConfig__()
        self.functions:Dict[str, __function__]  = {}
        self.variables  = {}

    def registerFunction(self, function, maxPending=0, maxTime=0):
        self.functions[function.__name__] = __function__(function, maxPending, maxTime)

    def registerFunctions(self, functions:list, maxPending=0, maxTime=0):
        for function in functions:
            self.functions[function.__name__] = __function__(function, maxPending, maxTime)

