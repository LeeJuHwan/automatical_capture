import cv2
import os

# settings.py
screenshot_files_path = "/Users/juhwan.lee/Desktop/temp/"  # Capture save directory path
screenshot_files_list = os.listdir(screenshot_files_path)
print(screenshot_files_list)
cropped_image_local_save_path = "/Users/juhwan.lee/Desktop/"
file_name = "screenshot"

if screenshot_files_list[0] == ".DS_Store":
    screenshot_files_list = screenshot_files_list[1:]

# util: module
def get_crop_size():
    print("start")
    first_screenshot_file = f"{screenshot_files_path}{screenshot_files_list[0]}"
    try:
        get_first_screenshot_file = cv2.imread(first_screenshot_file)
    except:
        print(f"Not exist image in your directory >> {screenshot_files_path}")

    X,Y,W,H = cv2.selectROI("location", get_first_screenshot_file, False)
    print(f"x: {X}, y: {Y}\nw: {W}, h: {H}")
    return X,Y,W,H

def image_crop(x,y,w,h):
    print(x,y,w,h)
    for increment, picture in enumerate(screenshot_files_list, start=1):
        
        img = cv2.imread(f"{screenshot_files_path}{picture}")
        cropped_image = img[y:y+h, x:x+w]
        cv2.imshow("img", cropped_image)
        cv2.imwrite(f"{cropped_image_local_save_path}screenshot{increment}.png",cropped_image)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    
    X,Y,W,H = get_crop_size()
    print("end")
    image_crop(X,Y,W,H)