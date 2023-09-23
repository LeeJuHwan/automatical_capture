from abc import ABCMeta, abstractmethod
import pynput
import time


class KeyboardController(metaclass=ABCMeta):
    def __init__(self):
        """
        Each operation systems use another hotkey
        MacOS: built-in capture program to fix frame size capture
        WindowOS: Full screen capture to clipboard    
        """
        self.controller = pynput.keyboard.Controller()
        self.keyboard_key = pynput.keyboard.Key

    def press_keys(self, keys):
        """실제 입력 할 키 배열을 받아 적용 합니다."""

        for key in keys:
            self.controller.press(key)

        time.sleep(0.1)

        for key in keys:
            self.controller.release(key)


    def keyboard_controll(self):
        """입력할 키보드 키 배열을 전달 합니다."""

        time.sleep(0.2)
        self.select_frame_size()
        time.sleep(0.2)
        self.take_a_screenshot()
        time.sleep(0.2)
        self.next_page()

    @abstractmethod
    def select_frame_size(self):
        """Capture screen box bounding"""

        # Mac OS
        # KEYBOARD_KEY.shift, KEYBOARD_KEY.cmd_l, pynput.keyboard.KeyCode.from_char("5")
        pass

    @abstractmethod
    def take_a_screenshot(self): 
        """Take a screenshot to keyboard button"""

        # Mac OS
        # KEYBOARD_KEY.enter
        pass

    @abstractmethod
    def next_page(self):
        """Take a screenshot after, next page"""
        
        # PDF web viewer
        # KEYBOARD_KEY.right
        pass