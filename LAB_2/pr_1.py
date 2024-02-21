from ev3dev2.motor import OUTPUT_A, LargeMotor
from time import sleep

motor = LargeMotor(OUTPUT_A)

for voltage in range(10, 51, 5):
    motor.run_direct(duty_cycle_sp=voltage)
    sleep(2)
    motor.stop()
    sleep(1)
for voltage in range(-51, -10, 5):
    motor.run_direct(duty_cycle_sp=voltage)
    sleep(2)
    motor.stop()
    sleep(1)