
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()
try:
    while True:

        humidity = sense.get_humidity()
        humidity= round(humidity,1)
        print("The humidity is:", humidity)

        temp=sense.get_temperature()
        temp=round(temp,1)
        print("The temperature is:", temp)

        pressure=sense.get_pressure()
        pressure=round(pressure,1)
        print("The pressure is :", pressure)

        time.sleep(5)

        sense.show_message("Temp:"+ str(temp)+ "Humidity:" + str(humidity) + "Pressure:" + str(pressure) , scroll_speed=0.1, text_colour=[255,0,255], back_colour=[0,0,0])

except KeyboardInterrupt:
              pass
        
