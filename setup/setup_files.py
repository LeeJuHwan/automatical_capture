import subprocess
from PIL import Image
import os
import shutil
from setup.setup_directory import create_screenshot_directory


def change_screenshot_file_name(flag):
    """
    스크린샷 파일명을 날짜 기준이 아닌 숫자로 변경 합니다.
    0 : 숫자 기준으로 변경
    1 : 날짜:시간 기준으로 변경
    """
    cmd = f'defaults write com.apple.screencapture "include-date" {flag}'
    subprocess.run(["/bin/bash", "-c", cmd])


def convert_rgb_images(screenshot_folder):
    """이미지 파일을 RGB값으로 변경 합니다."""
    images = [
        Image.open(os.path.join(screenshot_folder, files)).convert("RGB")
        for files in os.listdir(screenshot_folder)
    ]
    return images


def create_pdf_to_images(pdf_folder, images):
    """스크린샷 파일들을 하나의 PDF로 생성 합니다."""
    pdf_file_name = os.path.join(pdf_folder, "capture.pdf")
    images[0].save(pdf_file_name, save_all=True, append_images=images)


def remove_screenshot_files(screenshot_folder):
    """스크린샷 폴더에 있는 모든 파일을 삭제 합니다."""
    if os.path.exists(screenshot_folder):
        shutil.rmtree(screenshot_folder)

    create_screenshot_directory()
