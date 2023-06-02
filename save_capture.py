"""PDF viewr에서 각 페이지를 캡쳐 하는 반 자동화 프로세스"""
from setup import (
    setup_files,
    setup_optional_args as setup_option,
    setup_directory as setup_dir,
    setup_keyboard as setup_key,
)
import time


class Capture:
    def __init__(self):
        system_args = setup_option.optional()
        self.excute_after_wait_second = system_args.time
        self.count_of_pages = system_args.page
        self.is_remove_all_screenshot = bool(int(system_args.remove))

    def execute(self):
        setup_files.change_screenshot_file_name("0")
        SCREENSHOT_FOLDER = setup_dir.create_screenshot_directory()
        PDF_FOLDER = setup_dir.create_pdf_folder()

        setup_dir.setup_screenshot_directory(SCREENSHOT_FOLDER)
        setup_files.change_preview_options("false")
        time.sleep(self.excute_after_wait_second)
        for _ in range(self.count_of_pages):
            setup_key.keyboard_controll()

        images = setup_files.convert_rgb_images(SCREENSHOT_FOLDER)
        setup_files.create_pdf_to_images(PDF_FOLDER, images)

        setup_dir.reset_screenshot_directory()
        setup_files.change_screenshot_file_name("1")
        setup_files.change_preview_options("true")
        if self.is_remove_all_screenshot:
            setup_files.remove_screenshot_files(SCREENSHOT_FOLDER)


if __name__ == "__main__":
    capture = Capture()
    capture.execute()
