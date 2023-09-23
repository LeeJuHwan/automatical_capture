import subprocess
from PIL import Image
import os
import shutil
from .setup_directory import create_screenshot_directory
import re


def change_preview_options(boolean_param):
    """
    맥북 캡쳐시 썸네일 미리보기 옵션을 변경합니다.

    false: 썸네일 미리보기 끄기
    true: 썸네일 미리보기 켜기
    """
    cmd = f"defaults write com.apple.screencapture show-thumbnail -bool {boolean_param}"
    subprocess.run(["/bin/bash", "-c", cmd])


def change_screenshot_file_name(flag):
    """
    스크린샷 파일명을 날짜 기준이 아닌 숫자로 변경 합니다.
    0 : 숫자 기준으로 변경
    1 : 날짜:시간 기준으로 변경
    """
    cmd = f'defaults write com.apple.screencapture "include-date" {flag}'
    subprocess.run(["/bin/bash", "-c", cmd])


def extract_number(filename):
    """파일 이름에서 숫자를 추출하는 함수"""
    pattern = r"\d+"
    match = re.search(pattern, filename)
    if match:
        return int(match.group())
    return 0


def sort_screenshots(lst):
    """파일 이름에서 숫자를 추출하여 정렬하는 함수"""
    sorted_lst = sorted(lst, key=extract_number)
    return sorted_lst


def convert_rgb_images(screenshot_folder):
    """이미지 파일을 RGB값으로 변경 합니다."""
    sorted_screenshot_folder = sort_screenshots(os.listdir(screenshot_folder))

    images = [
        Image.open(os.path.join(screenshot_folder, files)).convert("RGB")
        for files in sorted_screenshot_folder
    ]

    return images


def create_pdf_to_images(pdf_folder, images):
    """스크린샷 파일들을 하나의 PDF로 생성 합니다."""
    pdf_file_name = os.path.join(pdf_folder, "capture.pdf")

    images[0].save(pdf_file_name, save_all=True, append_images=images[1:])


def remove_screenshot_files(screenshot_folder):
    """스크린샷 폴더에 있는 모든 파일을 삭제 합니다."""
    if os.path.exists(screenshot_folder):
        shutil.rmtree(screenshot_folder)

    create_screenshot_directory()
