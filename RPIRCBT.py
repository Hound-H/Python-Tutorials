from machine import Pin, PWM, time_pulse_us, UART
from utime import sleep_ms
import time

#----------Pin for motor driver--------------
ENA=Pin(14,Pin.OUT) #Activer le moteur A
ENB=Pin(15,Pin.OUT) #Activer le moteur B
IN1=Pin(3,Pin.OUT)
IN2=Pin(2,Pin.OUT)
IN3=Pin(5,Pin.OUT)
IN4=Pin(4,Pin.OUT)

pwm_A=PWM(ENA)
pwm_A.freq(500)

pwm_B=PWM(ENB)
pwm_B.freq(500)
#---------Pin for ultrasound-------
vitesse_son=343
trig=Pin(0,Pin.OUT)
echo=Pin(1,Pin.IN)
#-------Pin for servo motor-------
servo=PWM(Pin(6))
servo.freq(50)
vitesse = 0.5

def Forward(vitesse):
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    pwm_A.duty_u16(int(vitesse * 65535))
    pwm_B.duty_u16(int(vitesse * 65535))
    print(f"Calcul vitesse : {int(vitesse * 65535)}")

def Backward(vitesse):
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)
    pwm_A.duty_u16(int(vitesse * 65535))
    pwm_B.duty_u16(int(vitesse * 65535))

def Left(vitesse):
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    pwm_A.duty_u16(int(vitesse * 65535))
    pwm_B.duty_u16(int(vitesse * 65535))

def Right(vitesse):
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    pwm_A.duty_u16(int(vitesse * 65535))
    pwm_B.duty_u16(int(vitesse * 65535))
    
def Stop(vitesse):
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    pwm_A.duty_u16(int(vitesse * 65535))
    pwm_B.duty_u16(int(vitesse * 65535))

uart= UART(0,9600)

def Ultrason():
    global distance_cm
    trig.value(0)
    time.sleep_us(5)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    ultrason_duration=time_pulse_us(echo,1,30000) 
    distance_cm=vitesse_son*ultrason_duration/20000
    print(f"Distance : {distance_cm} Cm")
    time.sleep_ms(1000)
    return distance_cm

def controle():
    for mesure in range(1500,7500,3000):
        
        servo.duty_u16(mesure)
        
        print(mesure)
        balayage = ultra_son()
        time.sleep_ms(1000)
    
    
    for mesure in range(7500,1500,-3000):
        servo.duty_u16(mesure)
        print(mesure)
        balayage = ultra_son()
        time.sleep_ms(1000)

while True:
    if uart.any():
        data=uart.read()
        data=str(data)
        print(data)
        
        if("forward" in data):
            Forward(vitesse)
            
        elif("backward" in data):
            Backward(vitesse)
            
        elif("left" in data):
            Left(vitesse)
        
            
        elif("right" in data):
            Right(vitesse)
            
        elif('E' in data):
            speed=data.split("|")
            print("vitesse ",speed[1])
            vitesse = float(speed[1])/100
    
        else:
            Stop(vitesse) #Stop
            