from datetime import datetime
import threading
from essentials import socket_ops_v2, tokening
from typing import Callable, Dict, Union, List, Any
import time
from ..auth import BasicAuthenticator
from ..objects import serviceInfo, clients, baseObject, request_objects, UndeliverableError

class __connection_details__:
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port
        self.maxResponseTime = 5

class __service_client__(baseObject):
    def __init__(self, controller, serviceInfo:serviceInfo, connection:socket_ops_v2.Socket_Server_Client):
        self.controller:ServiceRXController     = controller
        self.serviceInfo                        = serviceInfo
        self.name                               = serviceInfo.name
        self.id                                 = serviceInfo.id
        self.config                             = serviceInfo.config
        self.connection                         = connection

        self.requests   = 0
        self.completed  = 0
        self.pending    = 0

    def callFunction(self, name:str, *args) -> Any:
        self.requests += 1
        self.pending += 1
        try:
            resp = self.connection.ask(
                request_objects.__function_invoke__(name, args),
                self.controller.connection.maxResponseTime
            )
            self.completed += 1
            self.pending -= 1
            return resp
        except TimeoutError:
            self.pending -= 1
            raise UndeliverableError("The service did not respond")
        except UndeliverableError as e:
            self.pending -= 1
            raise e
    
    @property
    def failureRate(self):
        return round(self.completed / self.requests, 2)

    @property
    def connected(self):
        return self.connection.running

class AuthorizedServicesList:
    def __init__(self, serviceNames=[]):
        self.serviceNames:List[str] = serviceNames

    def add(self, *names:str):
        self.serviceNames += names

    def check(self, name):
        return name in self.serviceNames

class __functions__:
    def __init__(self, clients=None):
        self.__functions__:Dict[str, List[__service_client__]] = {}
        self.__clients__:Dict[str, __service_client__] = {}
        if clients is not None:
            self.__clients__ = clients
            self.__update__()

    def __getattribute__(self, __name: str) -> Callable:
        if "__" not in __name and __name in self.__functions__:
            if self.__functions__[__name].__len__() == 0:
                raise UndeliverableError("There are no services to answer this call")
            while True:
                best = sorted(self.__functions__[__name], key=lambda cli : cli.pending, reverse=True)
                for client in best:
                    if client.pending >= client.serviceInfo.config.requests.maxPending:
                        continue
                    def wrapper(*args):
                        return client.callFunction(__name, *args)
                    return wrapper
                print(f"EVENT: Maximum pending has been reached! Service [\"{best[0].name}\"] && Function: ({__name})")
                time.sleep(0.25)
        try:
            return super().__getattribute__(__name)
        except:
            raise UndeliverableError("The requested function was not deliverable")


    def __repr__(self) -> str:
        funcs = ", ".join(list(self.__functions__.keys()))
        if len(funcs) > 20:
            funcs = funcs[:20] + "..."
        strs = f"< Function Addressing - Functions: {funcs} >"
        return strs

    def __update__(self, clients=None):
        print(self.__clients__)
        if clients is not None:
            self.__clients__ = clients
        for cli in self.__clients__:
            client = self.__clients__[cli]
            for func in client.serviceInfo.functions:
                if func not in self.__functions__:
                    self.__functions__[func] = []
                if client not in self.__functions__[func]:
                    self.__functions__[func].append(client)

        for func in self.__functions__:
            func = self.__functions__[func]
            toDel = []
            for client in func:
                if client.connected == False:
                    toDel.append(client)
            for client in toDel:
                func.remove(client)

class __service_group__:
    def __init__(self, controller, name:str, clients):
        self.name:str = name
        self.__controller__ = controller
        self.clients:Dict[str, __service_client__] = clients
        self.functions = __functions__(clients)
        #self.variables = __variables__(self)
        pass


class __service_list__:
    def __init__(self, controller):
        self.__controller__:ServiceRXController = controller
        self.__services__:Dict[str, __service_group__] = {}

    def __getitem__(self, __k:str) -> __service_group__:
        return self.__services__[__k]

    def get(self, serviceName):
        return self.__services__.get(serviceName)

    def __getattribute__(self, __name: str) -> __service_group__:
        if "__" not in __name and __name in self.__services__:
            return self.__services__[__name]
        try:
            return super().__getattribute__(__name)
        except:
            print(__name)
            raise LookupError("The requested service was not found")

    def __update__(self):
        for serv in self.__controller__.__clients__:
            self.__services__[serv] = __service_group__(self, serv, self.__controller__.__clients__[serv])

        servDel = []
        for serv in self.__services__:
            serv = self.__services__[serv]
            toDel:List[__service_client__] = []
            for client in serv.clients:
                client = serv.clients[client]
                if client.connected == False:
                    toDel.append(client)
            for client in toDel:
                del serv.clients[client.id]
            if serv.clients.__len__() == 0:
                servDel.append(serv.name)
        
        for serv in servDel:
            del self.__services__[serv]


class ServiceRXController:
    def __init__(self, host:str, port:int):
        self.serviceInfo = serviceInfo()
        self.serviceInfo.client = clients.python
        self.connection = __connection_details__(host, port)
        self.__clients__:Dict[str, Dict[str, __service_client__]] = {}
        self.authenticator:Union[None, BasicAuthenticator] = None
        self.authedServiceList:Union[None, AuthorizedServicesList] = None

        self.services = __service_list__(self)
    
    def blockUntilArrival(self, list:Union[AuthorizedServicesList, None], timeout:int=300):
        started = datetime.now()
        while True:
            if timeout != 0:
                if (datetime.now() - started).seconds >= timeout:
                    raise TimeoutError("Event: COA Timeout Error")
            go = True
            if list is None:
                if self.authedServiceList is None:
                    raise ValueError("Event: Block Until - Controller authedServiceList is None when param reqServices is None")
                checklist = self.authedServiceList.serviceNames
            else:
                checklist = list.serviceNames
            for sv in checklist:
                if sv not in self.__clients__:
                    go = False
                    break
            if go:
                break
            time.sleep(0.01)

    def commenceOnArrival(self, func, reqServices:Union[AuthorizedServicesList, None]=None, args:list=[], timeout:int=300):
        if reqServices is None:
            if self.authedServiceList is None:
                raise ValueError("Event: Block Until - Controller authedServiceList is None when param reqServices is None")
        def routine(controller:ServiceRXController, list:Union[AuthorizedServicesList, None], func, args:list, timeout:int):
            controller.blockUntilArrival(list, timeout)
            func(*args)
        threading.Thread(target=routine, daemon=True, args=[self, reqServices, func, args, timeout]).start()

    
    def __connected(self, connection:socket_ops_v2.Socket_Server_Client):
        time.sleep(2)
        if connection.meta.get('auth') is None:
            if connection.meta.get('service') is None:
                connection.shutdown()

    def __disconnect(self, connection:socket_ops_v2.Socket_Server_Client):
        if connection.meta['service']:
            service:serviceInfo = connection.meta['service']
            print("Service Module Disconnected")
            del self.__clients__[service.name][service.id]
            self.services.__update__()

    def __receiver(self, data:Union[str, dict], connection:socket_ops_v2.Socket_Server_Client):
        pass

    def __communicator(self, question:socket_ops_v2.Socket_Question):
        if type(question.data) == dict:
            if question.data.get('srx.action') is not None:
                action = question.data['srx.action']
                if action == "auth":
                    if self.authenticator is None:
                        question.answer(True)
                        return True
                    else:
                        try:
                            twoStep = self.authenticator.newChallenge()
                            authResp = question.questioner.ask({"srx.action": "auth", "data": twoStep.challenge})
                            question.answer(twoStep.validate(authResp))
                            return False
                        except:
                            question.answer(False)
                            return
                elif action == "init":
                    clientInit = serviceInfo().__loadJson__(question.data['data'])
                    serviceName = clientInit.name

                    if self.authedServiceList is not None:
                        resp = self.authedServiceList.check(serviceName)
                        if resp == False:
                            print(f"EVENT: An authorized Service named: [\"{serviceName}\"] tried to register but was rejected due to authedServiceList")
                            question.answer({"go away": True})
                            return "go away"
                    
                    if serviceName not in self.__clients__:
                        self.__clients__[serviceName] = {}

                    serviceID = tokening.CreateToken(4, self.__clients__[serviceName])
                    clientInit.id = serviceID

                    cli = __service_client__(self, clientInit, question.questioner)    
                    
                    self.__clients__[serviceName][serviceID] = cli  

                    question.questioner.meta['client'] = cli
                    question.questioner.meta['service'] = clientInit
                    question.answer({"resp": "welcome", "data": clientInit.__json__})
                    print("Welcomed Service:", f" [\"{clientInit.name}\"] - Version: ({clientInit.version}), ID: [\"{cli.id}\"]")
                    self.services.__update__()
                    return "welcome"
                        
    def start(self, blockUntil:Union[bool, AuthorizedServicesList]=False, timeout:int=300):
        self.server = socket_ops_v2.Socket_Server_Host(
            self.connection.host,
            self.connection.port,
            self.__connected,
            self.__receiver,
            self.__communicator,
            self.__disconnect,
            PYTHONIC_only=True,
        )
        print("Service RX Client Server:", self.connection.host, "Port:", self.connection.port)
        if blockUntil:
            if timeout == 0:
                print("Event: Waiting Indef. For Services to Subscribe")
            else:
                print("Event: Waiting For Services to Subscribe")
            self.blockUntilArrival(blockUntil, timeout)


