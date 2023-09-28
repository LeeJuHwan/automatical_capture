import cv2
from PIL import Image


class BoundingBoxWidget:
    def __init__(self):
        self.original_image = cv2.imread("/Users/juhwan.lee/Desktop/temp.png")
        self.clone = self.original_image.copy()

        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.extract_coordinates)

        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x, y)]

        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x, y))
            print(
                f"top left: {self.image_coordinates[0]}, bottom right: {self.image_coordinates[1]}"
            )
            print(
                f"x,y,w,h : ({self.image_coordinates[0][0]}, {self.image_coordinates[0][1]}, {self.image_coordinates[1][0] - self.image_coordinates[0][0]}, {self.image_coordinates[1][1] - self.image_coordinates[0][1]}"
            )

            # Draw rectangle
            cv2.rectangle(
                self.clone,
                self.image_coordinates[0],
                self.image_coordinates[1],
                (36, 255, 12),
                2,
            )
            cv2.imshow("image", self.clone)

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone

    def drag_pixel_size(self):
        return (
            self.image_coordinates[0][0],
            self.image_coordinates[0][1],
            self.image_coordinates[1][0] - self.image_coordinates[0][0],
            self.image_coordinates[1][1] - self.image_coordinates[0][1],
        )


if __name__ == "__main__":
    boundingbox_widget = BoundingBoxWidget()
    while True:
        cv2.imshow("image", boundingbox_widget.show_image())
        key = cv2.waitKey(1)

        # Close program with keyboard 'q'
        if key == ord("q"):
            x, y, w, h = boundingbox_widget.drag_pixel_size()
            cv2.destroyAllWindows()
            img = Image.open("/Users/juhwan.lee/Desktop/temp.png")
            crop_im = img.crop((x, y, w, h))
            crop_im.show()
            exit(1)
