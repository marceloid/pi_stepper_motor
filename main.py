# Código original retirado deste site: https://www.electronicshub.org/raspberry-pi-stepper-motor-control/
import RPi.GPIO as GPIO # https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/ Instruções do uso básico da biblioteca.
import time 

from enum import Enum

class Direcao(Enum):
    DIREITA = 0
    ESQUERDA = 1

class PiStepperMotor():
    def __init__(self) -> None:
        self.coil_1a = 11
        self.coil_1b = 13
        self.coil_2a = 12
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
        
    def volta_completa(self, direcao=Direcao.DIREITA):
        secs = 0.003
        combinacao = [
            (True, True, False, False),
            (False, True, True, False),
            (False, False, True, True),
            (True, False, False, True),
        ]
        if direcao == Direcao.ESQUERDA:
            combinacao.reverse()
        
        pinos = (
            self.coil_1a,
            self.coil_1b,
            self.coil_2a,
            self.coil_2b,
        )
        caminhada = 1
        while(caminhada <= 2048): # 2048 foi o que calculei para dar uma volta completa. Este site explica o porquê: https://arduinoinfo.mywikis.net/wiki/SmallSteppers#Test_Sketch:_Rotate_1_turn_in_each_direction.2C_repeat
            for passo in combinacao:
                GPIO.output(pinos, passo)
                self.delay(secs)
                caminhada = caminhada + 1


    def stop(self):
        print('Desligando o motor...')
        GPIO.cleanup()


if __name__ == '__main__':
    carpi = PiStepperMotor()

    carpi.set_pins(11, 13, 12, 15)
    carpi.volta_completa(direcao=Direcao.ESQUERDA)
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
