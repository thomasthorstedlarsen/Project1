#Lyskryds states:
#A1redA2red
#A1redyewllowA2red
#A1greenA2red
#A1yellowA2red
#A1redA2red2
#A1redA2redyellow
#A1redA2green
#A1redA2yellow
#A1redA2red

#Imports
from gpiozero import LED
from time import sleep
import random

#Lyskryds status definitioner:
A1red = LED(13)
A1yellow = LED(19)
A1green = LED(26)
A2red = LED(21)
A2yellow = LED(20)
A2green = LED(16)


#Start state:
def state0():
    return A1redA2red()

#Lyskryds states:

def A1redA2red():
    A2yellow.off()
    A1red.on()
    A2red.on()
    sleep(1)
    return A1redyellowA2red()

def A1redyellowA2red():
    A1yellow.on()
    sleep(1)
    return A1greenA2red()

def A1greenA2red():
    A1red.off()
    A1yellow.off()
    A1green.on()
    sleep(1)
    return A1yellowA2red()

def A1yellowA2red():
    A1green.off()
    A1yellow.on()
    sleep(1)
    return A1redA2red2()

def A1redA2red2():
    A1yellow.off()
    A1red.on()
    sleep(1)
    return A1redA2redyellow()

def A1redA2redyellow():
    A2yellow.on()
    sleep(1)
    return A1redA2green()

def A1redA2green():
    x=random.randrange(1,10)
    if x == 1:
      A1red.off()
      A2red.off()
      A2yellow.off()
      A1green.on()
      A2green.on()
      sleep(5)
      return A1redA2yellow()
    else:
      A2red.off()
      A2yellow.off()
      A2green.on()
      sleep(1)
      return A1redA2yellow()

def A1redA2yellow():
    A2green.off()
    A2yellow.on()
    sleep(1)
    return A1redA2red()


state=state0
while state: state=state()
