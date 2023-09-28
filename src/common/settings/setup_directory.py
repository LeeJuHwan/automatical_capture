import os
import subprocess
from pathlib import Path


WORKING_DIRECTORY = Path(os.path.dirname(__file__)).parent.parent.parent


def create_directory(file_name):
    """스크린샷을 저장 할 폴더를 생성 합니다."""

    create_directory_name = file_name
    capture_save_directory_path = os.path.join(WORKING_DIRECTORY, create_directory_name)

    if not os.path.exists(capture_save_directory_path):
        os.makedirs(capture_save_directory_path)

    return capture_save_directory_path


def setup_screenshot_directory(screenshot_folder):
    """스크린샷 파일을 저장 위치를 변경 합니다"""

    cmd = f"defaults write com.apple.screencapture location {screenshot_folder}"
    subprocess.run(["/bin/bash", "-c", cmd])


def reset_screenshot_directory():
    """임시로 변경 한 스크린샷 저장 위치를 기존으로 되돌립니다."""
    cmd = "defaults delete com.apple.screencapture location"
    subprocess.run(["/bin/bash", "-c", cmd])
    subprocess.run(["killall", "SystemUIServer"])


if __name__ == "__main__":
    print(WORKING_DIRECTORY)
