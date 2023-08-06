from ServiceRX.client import ServiceRXClient, Variables
import time
from PIL import Image

def readImage(file:str) -> Image.Image:
    Img = Image.open(file)
    return Img

# this function takes an file path and returns an image object class


s = ServiceRXClient() # Created the client

s.serviceInfo.name      = "dataStore"
s.serviceInfo.version   = "0.0.1"
s.serviceInfo.config.requests.maxPending = 5

s.serviceInfo.registerFunctions([readImage])
# Register which functions are to be allowed to be accessed remotely

s.setup('127.0.0.1', 5000) # Server address
s.connect()


time.sleep(50) # wait for this long. because im non blocking