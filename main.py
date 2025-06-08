def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P0, 270)
    basic.pause(5000)
    pins.servo_write_pin(AnalogPin.P0, 0)
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.analog_set_period(AnalogPin.P0, 2000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P3) == 0 or pins.digital_read_pin(DigitalPin.P3) == 0:
        pass
    if pins.digital_read_pin(DigitalPin.P2) == 0 or pins.digital_read_pin(DigitalPin.P2) == 0:
        pass
basic.forever(on_forever)
