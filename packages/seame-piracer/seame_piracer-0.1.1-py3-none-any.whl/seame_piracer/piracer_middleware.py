import os
import time
from piracer.vehicles import PiRacerStandard
from piracer.gamepads import ShanWanGamepad
from threading import Thread

class Piracer(object):
    def rc_control_thread(self):
        shanwan_gamepad = ShanWanGamepad()
        while True:
            gamepad_input = shanwan_gamepad.read_data()
            throttle = gamepad_input.analog_stick_right.y * self.mode
            steering = -gamepad_input.analog_stick_left.x

            # P R N D = 0 1 2 3
            if throttle == 0:
                if steering > 0 or steering < 0:
                    self.gear = 2 # Neutral
                else:
                    self.gear = 0 # Park
            elif throttle < 0:
                self.gear = 1 # Rear
            elif throttle > 0:
                self.gear = 3 # Drive

            # Gear Select
            if gamepad_input.button_y + gamepad_input.button_x + gamepad_input.button_a + gamepad_input.button_b == 1:
                if gamepad_input.button_y:
                    self.gear = 0
                elif gamepad_input.button_x:
                    self.gear = 1
                elif gamepad_input.button_a:
                    self.gear = 2
                elif gamepad_input.button_b:
                    self.gear = 3


            self.piracer.set_throttle_percent(throttle)
            self.piracer.set_steering_percent(steering)

    def __init__(self):
        self.piracer = PiRacerStandard()
        rc_thread = Thread(target=self.rc_control_thread)
        rc_thread.start()
        self.battery_voltage = 0
        self.battery = 0
        self.mode = 0.5
        self.gear = 0


    def get_mode(self):
        return self.mode * 10

    def get_gear(self):
        return self.gear

    def get_battery(self):
        self.battery_voltage = self.piracer.get_battery_voltage()
        self.battery = round((self.battery_voltage - 9) / 3.2 * 100)
        if self.battery < 0:
            self.battery = 0
        return self.battery

    def mode_select(self, smode:int):
        self.mode = smode / 10
        print("set mode: ", self.mode)

    def gear_select(self, sgear:int):
        self.gear = sgear
        print("set gear: ", self.gear)
