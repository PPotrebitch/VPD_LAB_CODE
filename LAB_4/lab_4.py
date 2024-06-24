import ev3dev2.motor as motor
import time
from math import pi, cos, sin, atan2


def sat(vol):
    if vol > 100:
        vol = 100
    elif vol < -100:
        vol = -100
    return vol


def angleSat(theta):
    if theta > pi:
        return theta - 2 * pi
    elif theta + pi < 0:
        return theta + 2 * pi
    else:
        return theta
    




DOTS = [(0.5, 0), (0.5, 0.5), (0, 0.5), (0, 0)]
R = 11.12 / 1000
BAZA = (145.55+22.25)/1000
H = 0.05
k_s = 285
k_r = 690


motor_L = motor.LargeMotor('outA') 
motor_R = motor.LargeMotor('outB')

startPositionleft = motor_L.position * pi / 180
startPositionright = motor_R.position * pi / 180

lastposleft = 0
lastposright = 0

x, y, th = 0, 0, 0
timeStart = time.time()
try:
    for xg, yg in DOTS:
        file = open("coord " + str(xg) + '_' + str(yg), 'w')
        while True:
            timeNow = time.time() - timeStart

            posleft = motor_L.position * pi / 180 - startPositionleft
            posright = motor_R.position * pi / 180 - startPositionright
            deltaposleft = posleft - lastposleft
            deltaposright = posright - lastposright

            x += (deltaposleft + deltaposright) * R * cos(th) / 2
            y += (deltaposleft + deltaposright) * R * sin(th) / 2
            th += (deltaposright - deltaposleft) * R / BAZA

            rho = ((x - xg) ** 2 + (y - yg) ** 2) ** 0.5
            psi = atan2(yg - y, xg - x)
            alpha = angleSat(psi - th)
            Us = sat(k_s * rho)
            Ur = sat(k_r * alpha)
            
            motor_L.run_direct(duty_cycle_sp=sat(Us - Ur))
            motor_R.run_direct(duty_cycle_sp=sat(Us + Ur))

            lastposleft = posleft
            lastposright = posright
            file.write(str(timeNow) + ',' + str(x) + ',' + str(y) + '\n')
            if rho < H:
                file.close()
                break
except:
    print('Bye!')
    motor_L.run_direct(duty_cycle_sp = 0)
    motor_R.run_direct(duty_cycle_sp = 0)
    file.close()
