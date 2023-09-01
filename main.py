def on_logo_pressed():
    global flag1, flag2, product, sonar2, number
    flag1 = 1
    flag2 = 0
    product = number
    music.play(music.create_sound_expression(WaveShape.NOISE,
            54,
            54,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    OLED.clear()
    OLED.write_num_new_line(product)
    OLED.write_string_new_line("OK?")
    OLED.write_string_new_line("Yes(left) or No(right)")
    while flag1 == 1:
        if input.button_is_pressed(Button.A):
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    1600,
                    1,
                    255,
                    0,
                    300,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.CURVE),
                music.PlaybackMode.UNTIL_DONE)
            flag1 = 2
        if input.button_is_pressed(Button.B):
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    200,
                    1,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.CURVE),
                music.PlaybackMode.UNTIL_DONE)
            flag1 = 0
    if flag1 == 2:
        basic.clear_screen()
        OLED.clear()
        OLED.write_string_new_line("Please put your coin.")
        while flag2 == 0:
            sonar2 = 0
            for index in range(10):
                sonar2 += sonar.ping(DigitalPin.P2, DigitalPin.P2, PingUnit.CENTIMETERS)
            if sonar2 / 10 < 5:
                OLED.clear()
                if number == 1:
                    radio.send_number(1)
                    basic.pause(500)
                if number == 2:
                    radio.send_number(2)
                    basic.pause(500)
                if number == 3:
                    radio.send_number(3)
                    basic.pause(500)
                if number == 4:
                    radio.send_number(4)
                    basic.pause(500)
                OLED.write_string_new_line("thank you!")
                basic.pause(500)
                pins.digital_write_pin(DigitalPin.P15, 0)
                basic.pause(3500)
                pins.digital_write_pin(DigitalPin.P15, 1)
                number = 1
                flag1 = 0
                flag2 = 1
    OLED.clear()
    OLED.write_string_new_line("Please select your")
    OLED.write_string_new_line("product Number.(1~4)")
    OLED.write_string_new_line(" ")
    OLED.write_string_new_line(" ")
    OLED.write_string_new_line("!!Press the button until you hear a sound!!")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

sonar2 = 0
product = 0
flag1 = 0
flag2 = 0
number = 0
radio.set_group(39)
number = 1
flag2 = 0
OLED.init(128, 64)
pins.digital_write_pin(DigitalPin.P15, 1)
OLED.write_string_new_line("Please select your")
OLED.write_string_new_line("product Number.(1~4)")
OLED.write_string_new_line(" ")
OLED.write_string_new_line(" ")
OLED.write_string_new_line("!!Press the button until you hear a sound!!")

def on_forever():
    global number
    if input.button_is_pressed(Button.A):
        if flag1 == 0:
            number = number - 1
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    200,
                    1,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.CURVE),
                music.PlaybackMode.UNTIL_DONE)
    if input.button_is_pressed(Button.B):
        if flag1 == 0:
            number = number + 1
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    400,
                    600,
                    255,
                    0,
                    100,
                    SoundExpressionEffect.WARBLE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.UNTIL_DONE)
    if number < 1:
        number = 1
    if number > 4:
        number = 4
    if flag1 != 2:
        basic.show_number(number)
basic.forever(on_forever)
