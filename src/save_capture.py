from common.settings import setup_optional_args as setup_option
import platform
from capture.capture_mac_os import CaptureMacOS
from capture.capture_windows_os import CaptureWindowsOS


class Capture:
    def __init__(self):
        system_args = setup_option.optional()
        self.excute_after_wait_second = system_args.time
        self.is_remove_all_screenshot = bool(int(system_args.remove))
        self.is_convert_images_to_pdf = bool(int(system_args.convert))

    def get_os(self):
        os_alias = {
            "Darwin": "Mac",
            "Windows": "Windows",
        }
        system_os = platform.system()
        # system_os = "Windows"

        return os_alias.get(system_os)

    def run(self):
        _callable = {"Mac": CaptureMacOS, "Windows": CaptureWindowsOS}

        cls_addr = _callable.get(self.get_os())
        instance = cls_addr(
            self.excute_after_wait_second,
            self.is_remove_all_screenshot,
            self.is_convert_images_to_pdf,
        )
        instance.execute()


def main():
    capture = Capture()
    capture.run()


if __name__ == "__main__":
    main()
