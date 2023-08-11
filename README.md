# automatical_capture_from_macOS_hotkey

### auto PDF Capture program
> 라이브러리
- pynput | keyboard handling
    - [공식문서](https://pynput.readthedocs.io/en/latest/keyboard.html)

> 코드 프로세스
- 사전 작업
    - shift + command + 5를 누르고, PDF의 캡쳐가 필요한 부분의 프레임을 맞춰줍니다. -> 이때, 프레임은 다음 페이지를 넘겼을 때도 전체가 나오게 유지 해야 합니다. 

    - 캡쳐 할 화면을 뷰어를 준비 합니다.

    
- 프로그램 실행 프로세스
    - 디렉터리
        - [ ] 스크린샷 파일 명을 변경 합니다.
        - [ ] 스크린샷 파일을 저장 할 폴더를 생성 합니다.
        - [ ] PDF를 저장 할 폴더를 생성 합니다.
        - [ ] 스크린샷 파일 저장 폴더를 지정 합니다.

    - 캡쳐 
        - 반복 페이지 개 수 만큼
            - [ ] Mac os의 캡쳐 단축키를 누릅니다.
            - [ ] 캡쳐 버튼을 누릅니다.
            - [ ] 다음 화면을 넘깁니다.

    - 이미지
        - [ ] 이미지 파일을 RGB형태로 변경합니다.
        - [ ] 이미지 파일들을 1개의 PDF로 생성합니다.
    
    - 초기화
        - [ ] 변경된 파일명, 스크린샷 저장 위치 등을 기존 값으로 변경 합니다.
        - [ ] 스크린샷 폴더에 있는 파일을 모두 삭제 합니다.
            - 이 때, 삭제를 원하지 않는다면 시스템 인자 값에서 값을 변경 하여 이를 방지 할 수 있습니다.

### 주의 할 점
- 단축키를 반복 실행 하는 프로그램이며, 코드를 실행 한 후 캡쳐 할 화면으로 전환 하여야 합니다.
- 경험상 사전 작업에 설정한 프레임이 PDF에 저장 될 사진이기 때문에 설정을 잘 하는 것이 중요합니다.


### 코드 작성자의 의도
- 반복 캡쳐가 필요한 상황에서 사용자 입력 값에 맞게 단축키를 눌러줄 수 있습니다. 이때, 단축키는 [setup_keyboard](https://github.com/LeeJuHwan/automatical_capture_macOS/blob/main/setup/setup_keyboard.py)에서 변경 할 수 있고 관련 내용은 라이브러리 공식 문서를 참고 하여 수정 할 수 있습니다.


### 실행
- git clone
- install library
    ```
    pip3 install -r requirments.txt
    ```
    
- python run
    - system arguments help command
        ```
        optional arguments:
        -h, --help            show this help message and exit
        -t TIME, --time TIME  Run process after wait time >> default = 1
        -p PAGE, --page PAGE  Count of pages in PDF viewr. this is most parameter
        -r {0,1}, --remove {0,1}
                                Is saved screenshot files remove all >> 0: keep 1: delete | default = 1

        -c {0,1}, --convert {0,1}
                                Is screenshot images to PDF >> 0: False 1: True | default = 1
        ```

    e.g -> want to customize value                    
    ```
    python3 save_capture.py -t 5 -p 1 -r 0 or 1 -c 0 or 1
    ```

    e.g2 -> using default value
    ```
    python3 save_capture.py -p 700
    ```
    

- shell script
  ```
  sh capture.py
  ```

파이썬을 직접적으로 커맨드 라인을 통해 실행 할 수 있지만, 쉘 스크립트를 통해 대화형 커널로 페이지를 입력 하는 방법도 사용 할 수 있습니다.

