input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    flag1 = 1
    flag2 = 0
    product = number
    music.play(music.createSoundExpression(WaveShape.Noise, 54, 54, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    OLED.clear()
    OLED.writeNumNewLine(product)
    OLED.writeStringNewLine("OK?")
    OLED.writeStringNewLine("Yes(left) or No(right)")
    while (flag1 == 1) {
        if (input.buttonIsPressed(Button.A)) {
            music.play(music.createSoundExpression(WaveShape.Square, 1600, 1, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
            flag1 = 2
        }
        if (input.buttonIsPressed(Button.B)) {
            music.play(music.createSoundExpression(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
            flag1 = 0
        }
    }
    if (flag1 == 2) {
        basic.clearScreen()
        OLED.clear()
        OLED.writeStringNewLine("Please put your card and wait a few minutes.")
        while (flag2 == 0) {
            sonar2 = 0
            for (let index = 0; index < 10; index++) {
                sonar2 += sonar.ping(
                DigitalPin.P2,
                DigitalPin.P2,
                PingUnit.MicroSeconds
                )
            }
            if (sonar2 / 10 < 3) {
                basic.showNumber(sonar2 / 10)
                OLED.clear()
                if (number == 1) {
                    radio.sendNumber(1)
                    basic.pause(500)
                }
                if (number == 2) {
                    radio.sendNumber(2)
                    basic.pause(500)
                }
                if (number == 3) {
                    radio.sendNumber(3)
                    basic.pause(500)
                }
                if (number == 4) {
                    radio.sendNumber(4)
                    basic.pause(500)
                }
                OLED.writeStringNewLine("thank you!")
                basic.pause(500)
                basic.pause(3500)
                number = 1
                flag1 = 0
                flag2 = 1
            }
        }
    }
    OLED.clear()
    OLED.writeStringNewLine("Please select your")
    OLED.writeStringNewLine("product Number.(1~4)")
    OLED.writeStringNewLine(" ")
    OLED.writeStringNewLine(" ")
    OLED.writeStringNewLine("!!Press the button until you hear a sound!!")
})
let sonar2 = 0
let product = 0
let flag1 = 0
let flag2 = 0
let number = 0
radio.setGroup(39)
number = 1
flag2 = 0
OLED.init(128, 64)
OLED.writeStringNewLine("Please select your")
OLED.writeStringNewLine("product Number.(1~4)")
OLED.writeStringNewLine(" ")
OLED.writeStringNewLine(" ")
OLED.writeStringNewLine("!!Press the button until you hear a sound!!")
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        if (flag1 == 0) {
            number = number - 1
            music.play(music.createSoundExpression(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
        }
    }
    if (input.buttonIsPressed(Button.B)) {
        if (flag1 == 0) {
            number = number + 1
            music.play(music.createSoundExpression(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        }
    }
    if (number < 1) {
        number = 1
    }
    if (number > 4) {
        number = 4
    }
    if (flag1 != 2) {
        basic.showNumber(number)
    }
})
