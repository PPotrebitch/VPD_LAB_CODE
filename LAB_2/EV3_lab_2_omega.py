#!/usr/bin/env python3
import ev3dev2.motor as motor
import time

motor_A = motor.LargeMotor(motor.OUTPUT_A)
for volt in range(-50, 51, 5):
    if -50 <= volt <= -10 or 10 <= volt <= 50:
        time_start = time.time()
        pos_start = motor_A.position
        name = "data" + str(volt) + ".txt"

        file = open(name, "w")
        while True:
            timeReal = time.time() - time_start
            motor_a.run_direct(duty_cycle_sp = volt)
            motor_pose = motor_A.position - pos_start
            motor_vel = motor_A.speed
            file.write(str(timeReal) + " " + str(motor_pose) + " " + str(motor_vel) + "\n")
            if timeReal > 1:
                motor_A.run_direct(duty_cycle_sp = 0)
                break

        file.close()
        time.sleep(1)
