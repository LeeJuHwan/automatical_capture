import pynput
import time
from common.settings import (
    setup_files,
    setup_directory as setup_dir,
    setup_keyboard as setup_key,
)

class CaptureMacOS(setup_key.KeyboardController):
    """using Mac OS hotkey"""

    def __init__(self, _time, _is_remove_screenshot, _is_convert_pdf, _pages):
        super().__init__()
        self.excute_after_wait_second = _time
        self.is_remove_all_screenshot = _is_remove_screenshot
        self.is_convert_images_to_pdf = _is_convert_pdf
        self.count_of_pages = _pages
    
    def select_frame_size(self):
        self.press_keys([self.keyboard_key.shift, self.keyboard_key.cmd_l, pynput.keyboard.KeyCode.from_char("5")])

    def take_a_screenshot(self):
        self.press_keys([self.keyboard_key.enter])

    def next_page(self):
        self.press_keys([self.keyboard_key.right])
    
    def execute(self):
        setup_files.change_screenshot_file_name("0")
        SCREENSHOT_FOLDER = setup_dir.create_screenshot_directory()
        PDF_FOLDER = setup_dir.create_pdf_folder()

        setup_dir.setup_screenshot_directory(SCREENSHOT_FOLDER)
        setup_files.change_preview_options("false")
        time.sleep(self.excute_after_wait_second)

        try:
            for _ in range(self.count_of_pages):
                self.keyboard_controll()

            if self.is_convert_images_to_pdf:
                images = setup_files.convert_rgb_images(SCREENSHOT_FOLDER)
                setup_files.create_pdf_to_images(PDF_FOLDER, images)

            setup_dir.reset_screenshot_directory()
            setup_files.change_screenshot_file_name("1")
            setup_files.change_preview_options("true")
            if self.is_remove_all_screenshot:
                setup_files.remove_screenshot_files(SCREENSHOT_FOLDER)
        
        except KeyboardInterrupt:
            print("키보드 인터럽트 발생")
            setup_files.remove_screenshot_files(SCREENSHOT_FOLDER)