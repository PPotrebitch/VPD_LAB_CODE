import ev3dev2.motor as motor
import time
motor_a = motor.LargeMotor(motor.OUTPUT_A)
volt = 100
try:
    timeStart = time.time()
    file = open("dataPod.scv", "w")
    while True:
        timeNow = time.time() - timeStart
        if motor_a.position > 0:
            motor_a.run_direct(duty_cycle_sp=volt)
            file.write(str(timeNow) + "," + str(pos)  + "\n")
        elif motor_a.position < 0:
            motor_a.run_direct(duty_cycle_sp= - volt)
            file.write(str(timeNow) + "," + str(pos)  + "\n")
        elif motor_a.position == 0:
            motor_a.run_direct(duty_cycle_sp=0)
            file.write(str(timeNow) + "," + str(pos)  + "\n")
            break
        elif timeNow > 10:
            motor_a.run_direct(duty_cycle_sp=0)
            break
            
except Exception as e:
    raise e
finally:
    motor_a.stop(stop_action = "brake")
    file.close()    