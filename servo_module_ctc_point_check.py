import time
from adafruit_servokit import ServoKit


kit = ServoKit(channels=16)

Right_Motor = 0
Left_Motor = 15

#Initial positions of Servomotors 
kit.servo[Right_Motor].angle = 45
kit.servo[Left_Motor].angle = 120
time.sleep(3)

value_both_right_single_tap = True
value_both_left_single_tap = True
value_both_right_double_tap = True
value_both_left_double_tap = True

duration_bw_2_Single_taps = 6
duration_bw_2_double_taps = 3
ctc_test_case = 3
no_of_times_ldt = 0

if (ctc_test_case == 1):
    #Right Single Tap
    while (value_both_right_single_tap):
        kit.servo[Right_Motor].angle = 45
        time.sleep(duration_bw_2_Single_taps)
        kit.servo[Right_Motor].angle = 80
        time.sleep(0.25)
elif (ctc_test_case == 2):
    #Left Single Tap new setup angles
     while (value_both_left_single_tap):
         kit.servo[Left_Motor].angle = 120
         time.sleep(duration_bw_2_Single_taps)
         kit.servo[Left_Motor].angle = 85
         time.sleep(0.25)
elif (ctc_test_case == 3):
    #Right Double Tap
     while (value_both_right_double_tap):
         kit.servo[Right_Motor].angle = 45
         no_of_times_ldt = no_of_times_ldt + 1
         print(no_of_times_ldt)
         time.sleep(duration_bw_2_double_taps)
         kit.servo[Right_Motor].angle = 80
         time.sleep(0.15)
         kit.servo[Right_Motor].angle = 45
         time.sleep(0.15)
         kit.servo[Right_Motor].angle = 80
         time.sleep(0.15)       
elif (ctc_test_case == 4):
    #Left Double Tap new setup
     while (value_both_left_double_tap):
         kit.servo[Left_Motor].angle = 120
         no_of_times_ldt = no_of_times_ldt + 1
         print(no_of_times_ldt)
         time.sleep(duration_bw_2_double_taps)
         kit.servo[Left_Motor].angle = 85
         time.sleep(0.15)
         kit.servo[Left_Motor].angle = 120
         time.sleep(0.15)
         kit.servo[Left_Motor].angle = 85
         time.sleep(0.15)