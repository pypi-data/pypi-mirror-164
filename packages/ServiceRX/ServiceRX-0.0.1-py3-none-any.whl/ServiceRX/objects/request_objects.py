from . import baseObject

class __variable_update__(baseObject):
    def __init__(self, name, value):
        self.name:str = name
        self.value = value

class __function_invoke__(baseObject):
    def __init__(self, name, args):
        self.name:str = name
        self.args:list = args