>>> import RPi.GPIO as GPIO
>>> from time import sleep
>>> GPIO.setmode (GPIO.BOARD)
>>> GPIO.setup (11,GPIO.OUT)
>>> while True:
	GPIO.output(11,True)
	time.sleep(2)
	GPIO.output(11,False)
	time.sleep(2)
	
