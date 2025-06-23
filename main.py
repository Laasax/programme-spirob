def protection_moteurs():
    if pins.digital_read_pin(DigitalPin.P3) >= 1000 or pins.digital_read_pin(DigitalPin.P3) <= 50:
        pins.analog_set_period(AnalogPin.P0, 0)
    if pins.digital_read_pin(DigitalPin.P2) >= 1000 or pins.digital_read_pin(DigitalPin.P2) <= 50:
        pins.analog_set_period(AnalogPin.P1, 0)

def on_button_pressed_a():
    position_tentacule(180)
    basic.pause(2000)
    position_tentacule(0)
    basic.pause(2000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    position_tentacule(90)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global roll
    serial.write_line("" + str((value)))
    if True:
        if name == "roll":
            roll = Math.map(value, -80, 80, 0, 180)
            if roll >= 180:
                roll += 180
            elif roll <= -180:
                roll += -180
            position_tentacule(roll)
radio.on_received_value(on_received_value)

def position_tentacule(degres: number):
    global off_set_moteurs
    off_set_moteurs = 5
    if degres >= 90:
        pins.servo_write_pin(AnalogPin.P0, degres - off_set_moteurs)
        pins.servo_write_pin(AnalogPin.P8, degres)
    elif degres <= 85:
        pins.servo_write_pin(AnalogPin.P0, degres)
        pins.servo_write_pin(AnalogPin.P8, degres + off_set_moteurs)
    else:
        pins.servo_write_pin(AnalogPin.P0, degres)
        pins.servo_write_pin(AnalogPin.P8, degres)
off_set_moteurs = 0
roll = 0
pins.servo_write_pin(AnalogPin.P0, 90)
pins.servo_write_pin(AnalogPin.P8, 90)
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
