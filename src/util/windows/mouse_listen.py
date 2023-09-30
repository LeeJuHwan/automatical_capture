from pynput import mouse
from typing import Optional, Tuple

class MouseController:
    def __init__(self):
        self.x: Optional[int] = None
        self.y: Optional[int] = None
        self.w: Optional[int] = None
        self.h: Optional[int] = None
        self.bounding_box_position: Tuple(int) = None

    def drag_listen(self):
        """on press left button to drag listner"""

        with mouse.Listener(on_click=self._on_press_button_to_drag) as listener:
            listener.join()
            

    def _on_press_button_to_drag(self, x: float, y: float, _: object, pressed: object):
        """top - left click, bottom - right click to bounding box"""

        if pressed:
            if not(self.x and self.y):
                print(f"Drag started at x: {x}, y: {y}")
                self.x, self.y = int(x), int(y)

            elif not(self.w and self.h):
                print(f"Drag ended at x: {x}, y:{y}")
                self.w = int(x - self.x)
                self.h = int(y - self.y)

                self.bounding_box_position = (self.x, self.y, self.w + abs(self.x), self.h + abs(self.y))
                print(f"bounding box: {self.bounding_box_position}")

                # return is listner do not stop
                return False


if __name__ == "__main__":
    capture = MouseController()
    a = capture.drag_listen()
    print(f"a: {a}")
