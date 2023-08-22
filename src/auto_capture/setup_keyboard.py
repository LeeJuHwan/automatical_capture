import pynput
import time


CONTROLLER = pynput.keyboard.Controller()
KEYBOARD_KEY = pynput.keyboard.Key


def press_keys(keys):
    """실제 입력 할 키 배열을 받아 적용 합니다."""
    for key in keys:
        CONTROLLER.press(key)

    time.sleep(0.1)

    for key in keys:
        CONTROLLER.release(key)


def keyboard_controll():
    """입력할 키보드 키 배열을 전달 합니다."""
    time.sleep(0.2)
    press_keys(
        [
            KEYBOARD_KEY.shift,
            KEYBOARD_KEY.cmd_l,
            pynput.keyboard.KeyCode.from_char("5"),
        ]
    )
    time.sleep(0.2)
    press_keys([KEYBOARD_KEY.enter])
    time.sleep(0.2)
    press_keys([KEYBOARD_KEY.right])
