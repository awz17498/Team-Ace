# Team : Ace
이름 | 역할
--- | --- |
김동현 | Leader |
서숭용 | Programming(DB) |
허찬 | Programming(GUI) |
송환욱 | Programming(AI) |
박종광 | Planning |
문아영 | Planning |
김동현 | Planning |
강민기 | Assistance |
김하민 | Assistance |
유태우 | Assistance |

# Project : 오파고
### 개요
오목 AI게임 오픈소스를 활용하여 내부 알고리즘을 이해하고 본 강의에서 배운 내용을 접목 시켜<br>
프로그래밍에 대한 폭넓은 이해와 팀워크를 배움에 목적을 둔 프로젝트 입니다.

### 적용 기술
  * DB
  * GUI
  * AI
  * ALGORITHM
  
### 앞으로 해야할 일
* [Git Readme 작성 요령 알아두기(markdown)](https://www.google.com/search?q=GIT+README&oq=git+RE&aqs=chrome.0.69i59j69i57j35i39j0i433i512j0i131i433i512j0i433i512l2j0i131i433i512j0i512l2.3303j0j15&sourceid=chrome&ie=UTF-8)
  * 발표 준비
  * 개인 메모
* [GUI : Pygame 모듈 이해](https://kkamikoon.tistory.com/129)
* Ace.py 주석 달아가며 공부(※코드에 커서 두고 Ctrl + 마우스 우클릭시, 참조 가능)
* Mockup
#### 다음 주 수업까지 | 11/17(水)
* 발표 준비(readme, mockup 등)
* 인원 역할 수정
* 표준화 되는대로 개인별 브랜치 개설 후 코딩 및 공부
* 11.10 **ace.py 파워셀로 실행시 간헐적 오류 해결**
```
PS C:\Users\SONG\Desktop\Team-Ace\Ace_Project> py main.py
pygame 2.1.0 (SDL 2.0.16, Python 3.10.0)
Traceback (most recent call last):
  File "C:\Users\SONG\Desktop\Team-Ace\Ace_Project\main.py", line 137, in <module>
    main.start()
  File "C:\Users\SONG\Desktop\Team-Ace\Ace_Project\main.py", line 116, in start
    if temp_x <= 420 and temp_y <= 420:
UnboundLocalError: local variable 'temp_x' referenced before assignment
```


### 구현하고자 하는 기능
* 시작 버튼을 통한 게임 시작
* 시작과 동시에 게임이 종료 될때 까지 시간 측정
  * 최소 시간 승리 랭킹 구현
* 졌을 경우 재도전 버튼을 통해 게임 재시작
* 이겼을 경우 승리 화면 생성
  * 승리 화면 이름 입력칸 생성
  * 이름 입력시 승리한 판에 대한 승리 시간 저장
* 저장된 기록들을 짧은 시간순으로 랭킹 표출

### Install
* GUI : Pygame
```ps
pip install pygame
```

### 프로그램 규칙
* 시간 제한 : X
* 승리 조건 : 5목 이상
* AI : 흑(先) | User : 백(後)
* 3 x 3 : 흑, 백 모두 禁
* 4 x 4 : 흑, 백 모두 可

### 프로그램 전개
1. 시작버튼을 누르면 흑(AI)이 먼저 돌을 놓습니다.
2. 마우스로 조작하여 백(User)이 돌을 놓습니다.
3. 승리조건을 만족하면 승리화면으로 넘어갑니다.
4. 승리자의 이름을 입력합니다.
5. 승리 또는 패배하면 재시작 버튼을 통해 재시작 할 수 있습니다.

### ScreenShot
![게임화면](https://user-images.githubusercontent.com/89123604/141059724-01156e5d-9e2a-41fd-bcd6-d53b7f3d6d7a.JPG)
![승리화면](https://user-images.githubusercontent.com/89123604/141059815-5bc91cd6-1a34-4d0e-a0eb-7c8348c13a82.JPG)
![승리후 순위등록](https://user-images.githubusercontent.com/89123604/141059817-fbe566d5-929e-4fb2-a435-f4bd4c618e12.JPG)
![순위화면](https://user-images.githubusercontent.com/89123604/141059804-d1d7d10d-7787-4f23-86a3-655b66bbc059.JPG)
![omok](https://user-images.githubusercontent.com/48282708/71707199-feb57e00-2e2b-11ea-9257-977c33195025.png)

### 오픈소스의 어려웠던 점
1. 오목판의 흐름을 판단할 방법
2. 모든 좌표의 가중치(ex : 승리조건을 만족하는 곳이면 큰 수)를 계산하여 가장 높은 가중치의 좌표를 두게함
3. 패턴을 미리 정해놓고 체크하며 가중치 계산<br>
![o1](https://user-images.githubusercontent.com/48282708/73593289-b8942d00-4545-11ea-886e-45d81ec643ad.png)

### 오픈소스의 개선할 점
1. 재시작 전 카운트 다운할 때, 마우스 이벤트 오류 수정
2. MinMax 알고리즘을 사용하여 더 많은 수 예측
3. 4 x 3 or 4 x 4를 할때, 띄워진 4를 3으로 인식해서 3 x 3으로 잘못 인식함.
4. 카운트다운 할때, quit 이벤트 안먹힘
