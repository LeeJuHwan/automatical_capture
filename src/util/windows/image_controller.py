import os
import PIL
from PIL import Image
import numpy as np
from typing import Optional, List
from common.settings import setup_files


class ImageProcessing:
    def __init__(self, os: str):
        self.images = []
        self._screenshot_dir: Optional[List[str]] = None
        self._current_image: os.path = None
        self._previous_image: os.path = None
        self.duplicate_limit = 0
        self.os = os

    def __eq__(self, __value: np.array) -> Optional[bool]:
        """Is same image pixel value"""

        try:
            _pixel_image: np.array = self.pillow_image_to_pixel(self.images[-1])
            return np.array_equal(_pixel_image, __value)

        except IndexError:
            return
    
    @property
    def screenshot_dir(self):
        return self._screenshot_dir

    @screenshot_dir.setter
    def screenshot_dir(self, _value):
        self._screenshot_dir = _value

    def add_in_list(self, __value: PIL):
        """List append pillow image object"""

        self.images.append(__value)

    def get_capture_image_to_pil(self) -> PIL:
        """Image file to pil object"""

        screenshot_dir_file_list = [
            i for i in os.listdir(self._screenshot_dir) if i not in ".DS_Store"
        ]

        # screenshot directory sorted ascending
        screenshot_dir_file_list: List[str] = setup_files.sort_screenshots(
            screenshot_dir_file_list
        )

        if screenshot_dir_file_list:
            self._current_image = self._get_capture_image("current", screenshot_dir_file_list)

        if len(screenshot_dir_file_list) >= 2:
            self._previous_image = self._get_capture_image("previous", screenshot_dir_file_list)

        return Image.open(self._current_image)

    def _get_capture_image(
        self, _state: str, screenshot_dir_file_list: List[str]) -> os.path:
        """Get captured image file in directory"""

        state = {
            "previous": 2,
            "current": 1,
        }

        _index_number = state.get(_state)

        _capture_image_file: str = screenshot_dir_file_list[
            len(screenshot_dir_file_list) - _index_number
        ]
        return os.path.join(self._screenshot_dir, _capture_image_file)

    def get_image_size(self, _image_file: os.path) -> int:
        """For compare with previous and current image bytes size"""

        return os.path.getsize(_image_file)

    def pillow_image_to_pixel(self, pillow_obj_image: PIL) -> np.array:
        """For compare with previous and current image pixel"""

        _pixel = np.array(pillow_obj_image)
        return _pixel

    def pillow_image_to_rgb(self, _image: PIL) -> PIL:
        """Before create pdf file to convert rgb"""

        return _image.convert("RGB")

    def array_to_pil(self, __val: np.array, save_file_name: str) -> os.path:
        array_to_pil_image = Image.fromarray(__val)
        
        pil_image_path = os.path.join(self._screenshot_dir, save_file_name)
        
        array_to_pil_image.save(pil_image_path)

        return pil_image_path

    def compare_same_to_prev_image(self, __value: np.array) -> bool:
        """compare"""

        is_same_pixel = self.__eq__(__value)
        is_same_size = lambda x, y: x == y  # noqa
        _result = False

        # If find the duplicate images
        if is_same_pixel:

            if self.os == "Windows":
                self._current_image = self.array_to_pil(__value, f"duplicate_{self.duplicate_limit}_1.png")
                print("current:", self._current_image)

                self._previous_image = self.array_to_pil(
                    self.pillow_image_to_pixel(self.images[-1]), f"duplicate_{self.duplicate_limit}_2.png"
                )
                print("prev:", self._previous_image)

            print("same pixel !")
            current_image_stat = self.get_image_size(self._current_image)
            prev_image_stat = self.get_image_size(self._previous_image)

            print(f"current file_name: : {self._current_image} size: {current_image_stat}")
            print(f"prev file_name: {self._previous_image} size: {prev_image_stat}")

            # Is duplicate images same bytes size -> same pixels but different text inside
            if _result := is_same_size(current_image_stat, prev_image_stat):
                print("same size !")
                self.duplicate_limit += 1
                os.remove(self._current_image)

        return _result


if __name__ == "__main__":
    img = ImageProcessing()
