
#imports, time, gpio for raspberry pi, cwii for wii remote control
import cwiid 
import time 
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Assigning pin values for each motor
Motor1A = 27
Motor1B = 24
Motor1Enable = 5

Motor2A = 6
Motor2B = 22
Motor2Enable = 17

#setup GPIO pins 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1Enable,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2Enable,GPIO.OUT)


#connecting to the Wiimote. This allows several attempts 
# as first few often fail. 
print('Press 1+2 on your Wiimote now...') 
wm = None 
i=2 
while not wm: 
  try: 
    wm=cwiid.Wiimote() 
  except RuntimeError: 
    if (i>10): 
      quit() 
      break 
    print ("Error opening wiimote connection") 
    print ("attempt " + str(i))
    i +=1 


#set Wiimote to report button presses and accelerometer state 
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK
 
#turn on led to show connected 
wm.led = 1





while True:
  
    if (wm.state['buttons'] & cwiid.BTN_2) and (wm.state['buttons'] & cwiid.BTN_UP):
        while (wm.state['buttons'] & cwiid.BTN_2) and (wm.state['buttons'] & cwiid.BTN_UP):
          #Left
          
          
          GPIO.output(Motor2A,GPIO.HIGH)
          GPIO.output(Motor2B,GPIO.LOW)
          GPIO.output(Motor2Enable,GPIO.HIGH)
          
           
         
          
          GPIO.output(Motor1A,GPIO.HIGH)
          GPIO.output(Motor1B,GPIO.LOW)
          GPIO.output(Motor1Enable,GPIO.HIGH)


        GPIO.output(Motor1Enable,GPIO.LOW)
        GPIO.output(Motor2Enable,GPIO.LOW)
        
    elif (wm.state['buttons'] & cwiid.BTN_2) and (wm.state['buttons'] & cwiid.BTN_DOWN):
       #Right
      None  
    
    elif (wm.state['buttons'] & cwiid.BTN_2):

        #Forwards
        while (wm.state['buttons'] & cwiid.BTN_2) and (wm.state['buttons'] & cwiid.BTN_LEFT):
          

          GPIO.output(Motor2A,GPIO.HIGH)
          GPIO.output(Motor2B,GPIO.LOW)
          GPIO.output(Motor2Enable,GPIO.HIGH)

          GPIO.output(Motor1A,GPIO.HIGH)
          GPIO.output(Motor1B,GPIO.LOW)
          GPIO.output(Motor1Enable,GPIO.HIGH)

        GPIO.output(Motor1Enable,GPIO.LOW)
        GPIO.output(Motor2Enable,GPIO.LOW)
  
        
    elif (wm.state['buttons'] & cwiid.BTN_1):
         #Backwards
      None

    elif (wm.state['buttons'] & cwiid.BTN_HOME):
      break


from subprocess import call
call("sudo shutdown -h now", shell=True)
  


   
