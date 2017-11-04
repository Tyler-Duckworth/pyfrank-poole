'''
 Basically the equivalent of RobotMap. Has the entire WOPR-JR values condensed into a single file

'''
class Chandra():
 controller = 0

 '''
   *
   * USB  #things not on the robot
   *
  '''
 '''
   *
   * CANS  #PWM
   *
  '''
 L0Motor = 2
 L1Motor = 3

 R0Motor = 0
 R1Motor = 1

 climbMotor = 4
 intakeMotor = 5
 stirMotor = 6

 shooterMotor = 7

 '''
   *
   * DIO
   *
   '''
 L_encoder_dio = {3, 2}
 R_encoder_dio = {1, 0}

 '''
   *
   * Analog
   *
   *

   *
   * Serial
   *
   '''
 ultrasonic_0 = 0

 gearboxHighGear = 4
 gearboxLowGear = 5

 gearGateOpen = 0
 gearGateClose = 1

 gear_intakeLower = 2
 gear_intakeTighten = 3
  # talonCANID = 3
 SQUARE = 1
 x= 2
 CIRCLE = 3
 TRIANGLE = 4

 lone = 5
 rone = 6

 ltwo = 7
 rtwo = 8

 SHARE = 9
 OPTIONS = 10

 # L3 and R3 are pressing L and R sticks down
 rthree = 11
 lthree = 12

 home = 13
 TOUCH_PAD = 14

 '''

   These are axes which return a double (not a boolean)

 '''


 STICK_LEFT_X_AXIS = 0
 STICK_LEFT_Y_AXIS = 1

 STICK_RIGHT_X_AXIS = 2
 STICK_RIGHT_Y_AXIS = 5

 L_TRIGGER_AXIS = 3
 R_TRIGGER_AXIS = 4

 #These two are not buttons but POV directions.
 D_PAD_X_AXIS = -1
 D_PAD_Y_AXIS = -1

 #measure of distance between centers of wheels left and right.
 WHEEL_DISTANCE = .45

 STICK_X_AXIS = 0
 STICK_Y_AXIS = 1
 STICK_ROT_AXIS = 2