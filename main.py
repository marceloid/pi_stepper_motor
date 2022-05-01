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
