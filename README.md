# automatical_capture

## take a screenshot using shortcut key

### Process
- Configuration
    - Need to enable the terminal in "easy of use"
      <br>
      <br>
          ![image](https://github.com/LeeJuHwan/automatical_capture_macOS/assets/118493627/72a795b6-bbd0-496e-9963-300e27c47528)

    - ready for the screen to be captured.

    
- Windows OS
    - screenshot
        - [x] Click top-left and bottom-right -> specify capture area
        - [x] `PIL: Image.Grab()`
        - [x] RGB color convert
        - [x] resizing & upscaling
        - [x] PIL object to save a list

- Mac OS
    - screenshot
        - [x] Change the folder where the screenshot will be saved
        - [x] Change the screenshot saving format
        - [x] Screenshot preview option turn off
        - [x] `cmd + shift + 5`: use shortcut key
            - Press shift + command + 5, and frame the part of the PDF that needs to be captured
        - [x] Open a saved screenshot
        - [x] PIL object to save a list

- Common
    - Find duplicate images
        1. Image object to pixel(numpy array) for compare
        2. `If step one true` -> Get image file byte size for compare
        3. `If step two true` -> remove image file, limit count increment
        4. `If limit == user-set limit number` -> End all captures, convert captured images to PDFs

    - Convert PDF
        1. PIL(RGB) object saving array[0] append array[1:]

- Teardown only MacOS
    - Reset options
        - [x] Change the changed filename, screenshot save location default
        - [x] Delete all files in the screenshots folder
            - if you don't want to delete, you can try add system argument `-r 0`

### Modify hotkeys
- [Go to mac OS python file](./src/capture/capture_mac_os.py)
    ```python
    def select_frame_size(self):
        self.press_keys(
            [
                self.keyboard_key.shift,
                self.keyboard_key.cmd_l,
                pynput.keyboard.KeyCode.from_char("5"),
            ]
        )

    def take_a_screenshot(self):
        self.press_keys([self.keyboard_key.enter])

    def next_page(self):
        self.press_keys([self.keyboard_key.right])
    ```
    - [Go to keyboard module](./src/common/settings/setup_keyboard.py)
      ```python
      def keyboard_controll(self):
    
            time.sleep(0.2)
            self.select_frame_size()
            time.sleep(0.2)
            self.take_a_screenshot()
            time.sleep(0.2)
            self.next_page()
      ```

- [Go to windows OS python file](./src/capture/capture_windows_os.py)
    ```python
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

    def keyboard_controll(self) -> PIL:  # override
        
        time.sleep(0.2)
        _img = self.take_a_screenshot()
        time.sleep(0.2)
        self.next_page()

        return _img
    ```


### Quick Start
- git clone
- install library
    ```
    pip3 install -r requirments.txt
    ```
    
- run
    - system arguments help command
        ```
        optional arguments:
        -h, --help            show this help message and exit
        -t TIME, --time TIME  Run process after wait time >> default = 1
        -r {0,1}, --remove {0,1}
                                Is saved screenshot files remove all >> 0: keep 1: delete | default = 1

        -c {0,1}, --convert {0,1}
                                Is screenshot images to PDF >> 0: False 1: True | default = 1
        ```

    - shell script
        ```
        PTYHON FILE PATH: [ /Users/juhwan.lee/Desktop/GitHub/automatical_capture_macOS/src/save_capture.py ] file excution  # python file abs path
        user OS: Mac  # check your os
        ============= [Mac OS] capture =============
        1: start capture program
        q: to quit
        ===============================
        choose index number: 
        >  1

        ========== Scripts list ==========
        1: PROGRAM EXECUTE
        2: MODIFY PARAMETER
        q: TO QUIT
        ===============================
        choose index number:
        > 
        ```
        - execute: get start
        - parameter: convert pdf and, delete all screenshot files option

