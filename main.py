from grovepi import *
#reloay on d4

pinMode(4,"OUTPUT")
digitalWrite(4,1)
print("Relay is on")
time.sleep(1)
digitalWrite(4,0)
print("Relay is off")


