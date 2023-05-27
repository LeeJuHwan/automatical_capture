import pynput
import time
import argparse

keyboard_button = pynput.keyboard.Controller()
keyboard_key = pynput.keyboard.Key


def optional():
    parser = argparse.ArgumentParser(
        description="System parameter by capture optional params"
    )
    parser.add_argument(
        "-t",
        "--time",
        default=1,
        type=int,
        help="Run process after wait time >> default = 1",
    )
    parser.add_argument(
        "-p",
        "--page",
        type=int,
        help="Count of pages in PDF viewr. this is most parameter",
    )

    args = parser.parse_args()

    return args


def press_keys(keys):
    for key in keys:
        keyboard_button.press(key)

    time.sleep(0.1)

    for key in keys:
        keyboard_button.release(key)


def keyboard_con():
    time.sleep(0.2)
    press_keys(
        [
            pynput.keyboard.Key.shift,
            pynput.keyboard.Key.cmd_l,
            pynput.keyboard.KeyCode.from_char("5"),
        ]
    )
    time.sleep(0.2)
    press_keys([pynput.keyboard.Key.enter])
    time.sleep(0.2)
    press_keys([pynput.keyboard.Key.right])


system_args = optional()
run_after_wait_second = system_args.time
count_of_page = system_args.page


if __name__ == "__main__":
    time.sleep(run_after_wait_second)
    for _ in range(count_of_page):  # PDF 페이지 개 수
        keyboard_con()
