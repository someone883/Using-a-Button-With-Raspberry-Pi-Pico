#importing libraries
from machine import Pin
import time
#making variables
butFinState=0
butPin=14
#making objects
myButton=Pin(butPin,Pin.IN,Pin.PULL_UP)
while True:
    butState=myButton.value() #<-- 1=OFF 0=ON
    #uncomment for word output
    """
    if butState == 1:
        butFinState="OFF"
    else:
        butFinState="ON"
    """
    print(butState) #<--Change "butState" to "butFinState" if word output wanted
    time.sleep_ms(100)