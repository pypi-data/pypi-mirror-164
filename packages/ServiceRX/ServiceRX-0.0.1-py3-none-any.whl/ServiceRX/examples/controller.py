from ServiceRX.controller import ServiceRXController, AuthorizedServicesList
import time
from PIL import Image


s = ServiceRXController('127.0.0.1', 5000)
s.connection.maxResponseTime = 30
s.authedServiceList = AuthorizedServicesList(['dataStore']) # We will only allow this service name to register as a client
s.start()
# Host a controller server

s.blockUntilArrival(services=AuthorizedServicesList(['dataStore']), timeout=60)
# Wait until you have a client with the datasource tag, max timeout of 60 seconds, this technically should be in a try catch

readImage = s.services.dataStore.functions.readImage
# convert the remote function to a local variable
# NOTE: This is not required but can help you.

img:Image.Image = readImage("foo.png")
# Run the function on the remore clients given the arguments and get the result
# NOTE: the result type stayed the same as it came from the client

img.save("bar.png")
# save the image on this side of things.