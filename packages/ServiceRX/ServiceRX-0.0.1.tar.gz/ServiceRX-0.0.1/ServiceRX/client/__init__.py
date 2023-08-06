from urllib import request
from essentials import socket_ops_v2
from typing import Dict, Union
from ..auth import BasicAuthenticator
from ..objects import serviceInfo, clients, UndeliverableError, Variables
from ..objects import request_objects

class __connection_details__:
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port
        self.config = socket_ops_v2.Configuration()

class ServiceRXClient:
    def __init__(self):
        self.serviceInfo = serviceInfo()
        self.serviceInfo.client = clients.python
        self.authenticator:Union[None, BasicAuthenticator] = None
        self.shutdown = False

    def setup(self, host, port):
        self.connection = __connection_details__(host, port)

        self.connection.config.server_PYTHONIC_only     = True
        self.connection.config.on_question              = self.__communicator
        self.connection.config.on_data_recv             = self.__receiver
        self.connection.config.on_connection_close      = self.__disconnected

        self.controller = socket_ops_v2.Socket_Connector(
            self.connection.host,
            self.connection.port,
            self.connection.config
        )

    def __disconnected(self):
        print("Disconnected from RX Controller")
    
    def __connected(self):
        if self.authenticator is not None:
            print("Verifying Auth")
            self.controller.ask({"srx.action": "auth"})

        try:
            init:dict = self.controller.ask({"srx.action": "init", "data": self.serviceInfo.__json__})
        except Exception as e:
            print("Controller did not welcome this service")
            raise e 

        if init.get("resp") == "welcome":
            if type(init['data']) == dict:
                self.serviceInfo.id = init['data']['id']
            elif isinstance(init['data'], serviceInfo):
                init:serviceInfo
                self.serviceInfo.id = init.id
            print(f"Registered to controller - ID: [\"{self.serviceInfo.id}\"]")

        else:
            self.controller.shutdown()
            print("Controller did not welcome this service")
            exit(1)

    def __receiver(self, data:Union[str, dict]):
        if type(data) == dict:
            if data.get('srx.action') is not None:
                if data['srx.action'] == "var_update":
                    self.serviceInfo.variables.__setattr__(data['data']['name'], data['data']['value'])
        elif isinstance(data, request_objects.__variable_update__):
            data:request_objects.__variable_update__
            self.serviceInfo.variables.__setattr__(data.name, data.value)
                    

    def __communicator(self, question:socket_ops_v2.Socket_Question):
        if type(question.data) == dict:
            if question.data.get('srx.action') is not None:
                if question.data['srx.action'] == "auth":
                    if self.authenticator is None:
                        question.answer(True)
                        return True
                    else:
                        try:
                            twoStep = self.authenticator.newChallenge()
                            authResp = question.questioner.ask(twoStep.challenge)
                            question.answer(twoStep.validate(authResp))
                            return False
                        except:
                            question.answer(False)
                            return
        elif isinstance(question.data, request_objects.__function_invoke__):
            data:request_objects.__function_invoke__ = question.data
            try:
                resp = self.serviceInfo.functions[data.name].__function__(*data.args)
                question.answer(resp)
            except Exception as e:
                question.answer(UndeliverableError(e))
                print("not ok")
                raise e
            return

    def connect(self):
        self.controller.connect()
        print("Connected to RX Controller Server")
        self.__connected()


