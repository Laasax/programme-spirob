function protection_moteurs () {
    if (pins.digitalReadPin(DigitalPin.P3) >= 1000 || pins.digitalReadPin(DigitalPin.P3) <= 50) {
        pins.analogSetPeriod(AnalogPin.P0, 0)
    }
    if (pins.digitalReadPin(DigitalPin.P2) >= 1000 || pins.digitalReadPin(DigitalPin.P2) <= 50) {
        pins.analogSetPeriod(AnalogPin.P1, 0)
    }
}
input.onButtonPressed(Button.A, function () {
    position_tentacule(180)
    basic.pause(2000)
    position_tentacule(0)
    basic.pause(2000)
})
input.onButtonPressed(Button.B, function () {
    position_tentacule(90)
})
radio.onReceivedValue(function (name, value) {
    serial.writeLine("" + (value))
    if (true) {
        if (name == "roll") {
            roll = Math.map(value, -80, 80, 0, 180)
            if (roll >= 180) {
                roll += 180
            } else if (roll <= -180) {
                roll += -180
            }
            position_tentacule(roll)
        }
    }
})
function position_tentacule (degres: number) {
    pins.servoWritePin(AnalogPin.P0, degres)
    pins.servoWritePin(AnalogPin.P8, degres)
}
let roll = 0
pins.servoWritePin(AnalogPin.P0, 90)
pins.servoWritePin(AnalogPin.P8, 90)
radio.setGroup(1)
basic.forever(function () {
	
})
