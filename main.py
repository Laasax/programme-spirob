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
    pins.servo_write_pin(AnalogPin.P0, 90)
    pins.servo_write_pin(AnalogPin.P8, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

def position_tentacule(degres: number):
    global off_set_moteurs
    off_set_moteurs = 15
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
pins.servo_write_pin(AnalogPin.P0, 90)
pins.servo_write_pin(AnalogPin.P8, 90)

def on_forever():
    pass
basic.forever(on_forever)
