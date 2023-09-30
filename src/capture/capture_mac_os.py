import numpy as np
import os
import PIL
import pynput
import time
from common.settings import (
    setup_files,
    setup_directory as setup_dir,
    setup_keyboard as setup_key,
)
from util.windows.image_controller import ImageProcessing


class CaptureMacOS(setup_key.KeyboardController):
    """using Mac OS shortcut key"""

    def __init__(self, _time, _is_remove_screenshot: int, _is_convert_pdf: int):
        super().__init__()
        self.excute_after_wait_second: int = _time
        self.is_remove_all_screenshot: int = _is_remove_screenshot
        self.is_convert_images_to_pdf: int = _is_convert_pdf
        self.image_processing: ImageProcessing = ImageProcessing("Mac")

    def select_frame_size(self):
        self.press_keys(
            [
                self.keyboard_key.shift,
                self.keyboard_key.cmd_l,
                pynput.keyboard.KeyCode.from_char("5"),
            ]
        )

    def take_a_screenshot(self):
        self.press_keys([self.keyboard_key.enter])

    def next_page(self):
        self.press_keys([self.keyboard_key.right])

    def execute(self):
        setup_files.change_screenshot_file_name("0")
        SCREENSHOT_FOLDER: os.path = setup_dir.create_directory("screenshot")
        PDF_FOLDER: os.path = setup_dir.create_directory("pdf")

        setup_dir.setup_screenshot_directory(SCREENSHOT_FOLDER)
        setup_files.change_preview_options("false")
        print(" === optional parameter setup === ")
        time.sleep(self.excute_after_wait_second)
        print(" === loading === ")

        exit_flag = False
        capture_pages = 0
        limit = 1

        try:
            print(" === get start program === ")
            while not exit_flag:
                self.keyboard_controll()
                self.image_processing.screenshot_dir = SCREENSHOT_FOLDER
                _img: PIL = self.image_processing.get_capture_image_to_pil()

                rgb_image: PIL = self.image_processing.pillow_image_to_rgb(_img)
                pixel_image: np.array = self.image_processing.pillow_image_to_pixel(
                    rgb_image
                )

                if not self.image_processing.compare_same_to_prev_image(pixel_image):
                    self.image_processing.add_in_list(rgb_image)
                    capture_pages += 1
                exit_flag: bool = self.image_processing.duplicate_limit == limit

            print(f"exit: {exit_flag}")
            print(f"total page: {capture_pages}")

        except KeyboardInterrupt:
            print("Keyboard Interrupt! >> remove all images")
            setup_files.remove_screenshot_files(SCREENSHOT_FOLDER)

        except Exception as e:
            print(f"ERROR! >> {e}")

        # optional parameter convert pdf
        if self.is_convert_images_to_pdf:
            setup_files.create_pdf_to_images(PDF_FOLDER, self.image_processing.images)

            setup_dir.reset_screenshot_directory()
            setup_files.change_screenshot_file_name("1")
            setup_files.change_preview_options("true")

        # optional parameter remove image files
        if self.is_remove_all_screenshot:
            setup_files.remove_screenshot_files(SCREENSHOT_FOLDER)
