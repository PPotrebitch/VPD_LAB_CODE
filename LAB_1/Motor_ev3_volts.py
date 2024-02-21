import ev3dev2.motor as motor
import time
motor_a = motor.LargeMotor(motor.OUTPUT_A)
vol = [100, 80, 60, 40, 20, -20, -40, -60, -80, -100]
try:
    for v in vol:
        timeStart = time.time()
        startPos = motor_a.position
        name = "data" + str(v)
        file = open(name, "w")
        while True:
            timeNow = time.time() - timeStart
            motor_a.run_direct(duty_cycle_sp=v)
            pos = motor_a.position - startPos
            file.write(str(timeNow) + "," + str(pos) + "," + str(motor_a.speed) + "\n")
            if timeNow > 1:
                motor_a.run_direct(duty_cycle_sp=0)
                time.sleep(1)
                break
            
except Exception as e:
    raise e
finally:
    motor_a.stop(stop_action = "brake")
    file.close()
