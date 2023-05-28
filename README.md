# automatical_capture_macOS

### auto PDF Capture program
> 라이브러리
- pynput | keyboard handling
    - [공식문서](https://pynput.readthedocs.io/en/latest/keyboard.html)

> 코드 프로세스
- 사전 작업
    - shift + command + 5를 누르고, PDF의 캡쳐가 필요한 부분의 프레임을 맞춰줍니다. -> 이때, 프레임은 다음 페이지를 넘겼을 때도 전체가 나오게 유지 해야 합니다. 

    - 불필요한 옵션을 제거 합니다. -> 미리보기 썸네일 체크 해제, 마우스 포인터 보기 체크 해제

    
- 프로그램 실행 프로세스
    - 디렉터리
        1. 스크린샷 파일 명을 변경 합니다.
        2. 스크린샷 파일을 저장 할 폴더를 생성 합니다.
        3. PDF를 저장 할 폴더를 생성 합니다.
        4. 스크린샷 파일 저장 폴더를 지정 합니다.

    - 캡쳐 
        - 반복 페이지 개 수 만큼
            1. Mac os의 캡쳐 단축키를 누릅니다.
            2. 캡쳐 단축키를 누릅니다.
            3. 다음 화면을 넘깁니다.

    - 이미지
        1. 이미지 파일을 RGB형태로 변경합니다.
        2. 이미지 파일들을 1개의 PDF로 생성합니다.
    
    - 초기화
        1. 변경된 파일명, 스크린샷 저장 위치 등을 기존 값으로 변경 합니다.
        2. 스크린샷 폴더에 있는 파일을 모두 삭제 합니다.
            - 이 때, 삭제를 원하지 않는다면 시스템 인자 값에서 값을 변경 하여 이를 방지 할 수 있습니다.

### 주의 할 점
- 이 프로그램은 단축키를 이용하여 반복 하는 작업이기 때문에, 초기 프레임 설정을 기가 막히게 해주셔야 합니다. 다음 버튼을 눌렀을 때 화면이 초기화 되지 않고 설정한 프레임이 유지 된다면 이 프로그램을 작동 했을 땐 원하는 캡쳐기능을 이용 할 수 있습니다.


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
        ```

    e.g                    
    ```
    python3 save_capture.py -t 5 -p 1 -r 0 or 1
    ```
