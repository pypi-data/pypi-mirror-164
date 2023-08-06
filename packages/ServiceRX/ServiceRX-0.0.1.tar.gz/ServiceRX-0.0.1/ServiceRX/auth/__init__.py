from hashlib import md5
import random
from essentials import tokening, TimeStamp
from typing import Dict

class __user:
    def __init__(self):
        pass

class UserAuthenticator:
    def __init__(self):
        self.users:Dict[str, __user] = {}

    def createUser(self, username, password, access):
        pass

    def save(path=".srx/auth.ppy"):
        pass

    def load(path=".srx/auth.ppy"):
        pass

class __challenge:
    def __init__(self, __noise, __dir, __ts):
        self.noise = __noise
        self.dir = __dir
        self.timestamp = __ts

    @property
    def json(self):
        return {"noise": self.noise, "dir": self.dir, "ts": self.timestamp}

class twoStepAuthentication:
    def __init__(self, password):
        self.password = password
        self.__noise = [tokening.AssembleToken(5), tokening.AssembleToken(5), tokening.AssembleToken(5)]
        self.__dir = [random.randint(0, len(self.__noise-1)), random.randint(0, len(self.__noise-1)), random.randint(0, len(self.__noise-1))]
        self.__timestamp = TimeStamp()
        self.challenge = __challenge(self.__noise, self.__dir, self.__timestamp)

    @property
    def __construct(self):
        strs = []
        for x in self.__dir:
            strs += self.__noise[x]
        return str(self.__timestamp).join(strs)

    def validate(self, challengeResp):
        return md5(self.__construct).digest().decode() == challengeResp


class BasicAuthenticator:
    def __init__(self, password):
        self.password = password
    
    def newChallenge(self):
        return twoStepAuthentication(self.password)