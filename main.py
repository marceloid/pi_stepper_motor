# Código original retirado deste site: https://www.electronicshub.org/raspberry-pi-stepper-motor-control/
from turtle import delay
import RPi.GPIO as GPIO # https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/ Instruções do uso básico da biblioteca.
import time 
import itertools

class PiStepperMotor():
    def __init__(self) -> None:
        # Original
        # out1 = 13
        # out2 = 11
        # out3 = 15
        # out4 = 12

        self.coil_1a = 11
        self.coil_1b = 12
        self.coil_2a = 13
        self.coil_2b = 15
        print(GPIO.RPI_INFO)
        

    def set_pins(self, pin_1a, pin_1b, pin_2a, pin_2b):
        self.coil_1a = pin_1a
        self.coil_1b = pin_1b
        self.coil_2a = pin_2a
        self.coil_2b = pin_2b

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.coil_1a,GPIO.OUT)
        GPIO.setup(self.coil_1b,GPIO.OUT)
        GPIO.setup(self.coil_2a,GPIO.OUT)
        GPIO.setup(self.coil_2b,GPIO.OUT)

        GPIO.output(self.coil_1a,GPIO.LOW)
        GPIO.output(self.coil_1b,GPIO.LOW)
        GPIO.output(self.coil_2a,GPIO.LOW)
        GPIO.output(self.coil_2b,GPIO.LOW)
    
    def delay(self, secs):
        time.sleep(secs)
        
    def step(self):
        # time_ini = time.time()
        secs = 0.003
        combinacao = [
            (True, True, False, False),
            (False, True, True, False),
            (False, False, True, True),
            (True, False, False, True),
        ]
        
        pinos = (
            self.coil_1a,
            self.coil_1b,
            self.coil_2a,
            self.coil_2b,
        )
        caminhada = 0
        while(caminhada <= 4096):
            for passo in combinacao:
                GPIO.output(pinos, passo)
                delay(secs)
                caminhada = caminhada + 1
        # while(time.time() - time_ini < 10):
        #     GPIO.output(self.coil_1a,GPIO.HIGH)
        #     GPIO.output(self.coil_1b,GPIO.HIGH)
        #     GPIO.output(self.coil_2a,GPIO.LOW)
        #     GPIO.output(self.coil_2b,GPIO.LOW)
        #     self.delay(secs)
        #     GPIO.output(self.coil_1a,GPIO.LOW)
        #     GPIO.output(self.coil_1b,GPIO.HIGH)
        #     GPIO.output(self.coil_2a,GPIO.HIGH)
        #     GPIO.output(self.coil_2b,GPIO.LOW)
        #     self.delay(secs)
        #     GPIO.output(self.coil_1a,GPIO.LOW)
        #     GPIO.output(self.coil_1b,GPIO.LOW)
        #     GPIO.output(self.coil_2a,GPIO.HIGH)
        #     GPIO.output(self.coil_2b,GPIO.HIGH)
        #     self.delay(secs)
        #     GPIO.output(self.coil_1a,GPIO.HIGH)
        #     GPIO.output(self.coil_1b,GPIO.LOW)
        #     GPIO.output(self.coil_2a,GPIO.LOW)
        #     GPIO.output(self.coil_2b,GPIO.HIGH)
        #     self.delay(secs)
            #print(f'{passo}º passo...')
            #passo = passo + 1
    
    def stop(self):
        print('Desligando o motor...')
        GPIO.cleanup()


if __name__ == '__main__':
    carpi = PiStepperMotor()

    carpi.set_pins(11, 12, 13, 15)
    carpi.step()
    carpi.stop()

# i=0
# positive=0
# negative=0
# y=0



# try:
#    while(1):
#       GPIO.output(out1,GPIO.LOW)
#       GPIO.output(out2,GPIO.LOW)
#       GPIO.output(out3,GPIO.LOW)
#       GPIO.output(out4,GPIO.LOW)
#       x = int(input())
#       if x>0 and x<=4000:
#           for y in range(x,0,-1):
#               if negative==1:
#                   if i==7:
#                       i=0
#                   else:
#                       i=i+1
#                   y=y+2
#                   negative=0
#               positive=1
#               #print((x+1)-y)
#               if i==0:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==1:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==2:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==3:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==4:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==5:
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.HIGH)
#                   delay()
#               elif i==6:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
#                   delay()
#               elif i==7:    
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
#                   delay()
#               if i==7:
#                   i=0
#                   continue
#               i=i+1
      
      
#       elif x<0 and x>=-4000:
#           x=x*-1
#           for y in range(x,0,-1):
#               if positive==1:
#                   if i==0:
#                       i=7
#                   else:
#                       i=i-1
#                   y=y+3
#                   positive=0
#               negative=1
#               if i==0:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==1:
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==2:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==3:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.HIGH)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==4:  
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.LOW)
#                   delay()
#               elif i==5:
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.HIGH)
#                   GPIO.output(out4,GPIO.HIGH)
#                   delay()
#               elif i==6:    
#                   GPIO.output(out1,GPIO.LOW)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
#                   delay()
#               elif i==7:    
#                   GPIO.output(out1,GPIO.HIGH)
#                   GPIO.output(out2,GPIO.LOW)
#                   GPIO.output(out3,GPIO.LOW)
#                   GPIO.output(out4,GPIO.HIGH)
#                   delay()
#               if i==0:
#                   i=7
#                   continue
#               i=i-1 

              
# except:
#     GPIO.cleanup()
