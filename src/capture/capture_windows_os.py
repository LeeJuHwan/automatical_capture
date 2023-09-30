import numpy as np
import os
import pyautogui as pg
import PIL
from PIL import ImageGrab, Image
import time
from common.settings import (
    setup_files,
    setup_directory as setup_dir,
    setup_keyboard as setup_key,
)
from util.windows.image_controller import ImageProcessing
from util.windows.mouse_listen import MouseController


class CaptureWindowsOS(setup_key.KeyboardController):
    """using Windows OS shortcut key"""

    def __init__(self, _time, _is_remove_screenshot: int, _is_convert_pdf: int):
        super().__init__()
        self.excute_after_wait_second: int = _time
        self.is_remove_all_screenshot: int = _is_remove_screenshot
        self.is_convert_images_to_pdf: int = _is_convert_pdf
        self.image_processing: ImageProcessing = ImageProcessing("Windows")
        self.mouse_controller: MouseController = MouseController()

    def select_frame_size(self):
        self.mouse_controller.drag_listen()
        time.sleep(0.2)

    def take_a_screenshot(self) -> PIL:
        _img = ImageGrab.grab(self.mouse_controller.bounding_box_position)  # screen capture -> PIL Object
        new_size = (_img.width*2, _img.height*2)
        better_quality_image = _img.resize(new_size, Image.LANCZOS)
        return better_quality_image

    def next_page(self):
        self.press_keys([self.keyboard_key.right])
    
    def keyboard_controll(self) -> PIL:
        """입력할 키보드 키 배열을 전달 합니다."""
        time.sleep(0.2)
        _img = self.take_a_screenshot()
        time.sleep(0.2)
        self.next_page()

        return _img

    def execute(self):
        SCREENSHOT_FOLDER: os.path = setup_dir.create_directory("screenshot")
        PDF_FOLDER: os.path = setup_dir.create_directory("pdf")

        time.sleep(self.excute_after_wait_second)
        print(" === loading === ")

        exit_flag = False
        capture_pages = 0
        limit = 1

        try:
            print(" === get start program === ")
            self.select_frame_size()
            while not exit_flag:
                _img = self.keyboard_controll()
                self.image_processing.screenshot_dir = SCREENSHOT_FOLDER
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
            pg.alert("\n\n\n\n\n\nPDF 파일이 생성 되었습니다.\n\n\n\n\n")

        # optional parameter remove image files
        if self.is_remove_all_screenshot:
            setup_files.remove_screenshot_files(SCREENSHOT_FOLDER)


if __name__ == "__main__":
    capture = CaptureWindowsOS(1, 1, 1)
    