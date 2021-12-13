# Team : Ace
번호 | 이름 | 역할 | 비고 |
--- | --- | --- | --- |
1 | 서숭용 | Programming(DB) | - |
2 | 허찬 | Programming(pygame) | - |
3 | 송환욱 | Programming(AI) | - |
4 | 박종광 | Planning | - |
5 | 문아영 | Planning | - |
6 | 김동현 | Planning | Leader |
7 | 강민기 | Assistance | - |
8 | 김하민 | Assistance | - |
9 | 유태우 | Assistance | - |

# Project : 오파고
#### 기획 내용
오목 AI게임 오픈소스를 활용하여 내부 알고리즘을 이해하고 본 강의에서 배운 내용을 접목 시켜 
프로그래밍에 대한 폭넓은 이해와 팀워크를 배움에 목적을 둔 프로젝트 입니다.
* 적용 기술
  * DB
  * GUI
  * AI
  
#### 앞으로 해야할 일
* pygame 모듈에 대한 공부[https://kkamikoon.tistory.com/129]

#### 구현하고자 하는 기능
* 시작 버튼을 통한 게임 시작
* 시작과 동시에 게임이 종료 될때 까지 시간 측정
  * 최소 시간 승리 랭킹 구현
* 졌을 경우 재도전 버튼을 통해 게임 재시작
* 이겼을 경우 승리 화면 생성
  * 승리 화면 이름 입력칸 생성
  * 이름 입력시 승리한 판에 대한 승리 시간 저장
* 저장된 기록들을 짧은 시간순으로 랭킹 표출

------------
## Cording
##### - python version : 3.7
##### - encoding : UTF-8
### Install
#### GUI : Pygame
##### * --pip3 install pygame
------------
## Rule
##### - AI : 흑, User : 백
##### - 승리조건 : 5목 이상 (6목,, 7목 ... 등등)
##### - 3 x 3 : 흑,백 모두 금지
##### - 4 x 4 : 흑,백 모두 가능
##### - 시간제한 : 없음
## Start
##### 1. 시작버튼을 누르면 흑(AI)이 먼저 돌을 놓습니다.
##### 2. 마우스로 백(User)이 놓을 곳을 선택합니다.
##### 3. 승리조건을 만족하면 승리화면으로 넘어갑니다.
##### 4. 승리자의 이름을 입력합니다.
##### 5. 승리자의 이름을 입력을 하면 기록과 함께 순위표가 생성됩니다.
##### 6. 승리하면 재시작 버튼을 통해 재시작을 할 수 있습니다.
##### 7. 패배하면 재시작 버튼을 통해 재시작을 할 수 있습니다.



------------
## ScreenShot
### 실행화면
![omok](https://user-images.githubusercontent.com/48282708/71707199-feb57e00-2e2b-11ea-9257-977c33195025.png)
### 패배화면
![최최종 패배](https://user-images.githubusercontent.com/89123613/143179370-b3af6739-595d-4e64-8b77-932bb8e843f9.JPG)
### 승리화면
![최최종 승리](https://user-images.githubusercontent.com/89123613/143179363-44e6a02e-4132-443f-b6a4-7f405b6ebd02.JPG)
### 순위등록화면
![승리후 순위등록](https://user-images.githubusercontent.com/89123604/141059817-fbe566d5-929e-4fb2-a435-f4bd4c618e12.JPG)
### 순위화면
![랭킹 최종](https://user-images.githubusercontent.com/89123613/143179355-5aad8886-dcfb-4e8b-bd62-77642749e66b.JPG)


------------
## Memo
## 어려웠던 점
##### 1. 처음 사용해보는 Python GUI의 어려움
##### 2. 오목판의 흐름을 판단할 방법
##### - 모든 좌표의 가중치(ex : 승리조건을 만족하는 곳이면 큰 수)를 계산하여 가장 높은 가중치의 좌표를 두게함
![o1](https://user-images.githubusercontent.com/48282708/73593289-b8942d00-4545-11ea-886e-45d81ec643ad.png)
##### - 패턴을 미리 정해놓고 체크하며 가중치 계산

## 개선할 점
##### 1. 재시작 전 카운트 다운할 때, 마우스 이벤트 오류 수정
##### 2. MinMax 알고리즘을 사용하여 더 많은 수 예측
##### 3. 4 x 3 or 4 x 4를 할때, 띄워진 4를 3으로 인식해서 3 x 3으로 잘못 인식함.
##### 4. 카운트다운 할때, quit 이벤트 안먹힘
##### 5. 최좌측, 최상단 유저 돌 입력 안됨


## 개선한 점
##### 1. 파워쉘 이용시 간혈적 오류발생 (개선완료) - 게임시작시 변수인 teep_x, teep_y의 값을 초기화시키는 코딩 입력








# 2021년 12월 13일 프로젝트 마무리

## 프로젝트명 Team-Ace 오파고
> AI알고리즘을 활용한 오픈 소스를 통해 pygame으로 오목 게임을 실행합니다.

* DB와 GUI를 활용하여 AI를 구현하여 흑수 (AI)와 백수 (USER)의 오목을 진행하는 형식
* 기존 3 X 3룰과 승리공식을 통한 CHEAK POINT로 승리 및 패배 결과를 도출
* 랭킹 시스템 도입 (개발 중 / 미완료)

### 설치 방법

PYTHON3 - PYGAME

```py
pip install pygame
```

## 업데이트 내역

* 0.1.0 (21/11/05)
    * .exe 파일형태의 분할된 class를 main클래스로 병합하여 .exe 형태를 변경 (Console 에서 실행 가능)
* 0.1.1 (21/11/11)
    * 승리, 패배화면 mokup 파일 생성
    * 병합형태에서의 temp x,y 변수 로컬 지정으로 인한 오류 발생 / (개선 : temp변수 글로벌화 지정)
```
PS C:\Users\SONG\Desktop\Team-Ace\Ace_Project? py main.py
pygame 2.1.0 (SDL 2.0.16, Python 3.10.0)
Traceback (most recent call last):
   File "C:\Users\SONG\Desktop\Team-Ace\Ace_Project\main.py", line 137, in <module>
      main.start()
   File "C:\Users\SONG\Desktop\Team-Ace\Ace_Project\main.py", line 116, in start
      if temp_x <= 420 and temp_y <= 420:
UnboundLocalError: local variable 'temp_x' referenced before assignment
```
* 0.1.2 (21/11/18)
    * 기본 GUI 개념 학습 -> PYGAME 연동
    * DB 구현화를 위한 MYSQL, SQLITE 개념 학습
* 0.2.0 (21/11/25)
    * 오목 Game, pygame으로 구동 시작 및 버그 관련 정보 확인
       버그 1. 최상단, 최좌측 Users 착수 불가능 (미해결)
       버그 2. Game 승리 및 패배화면 도출 중 오목판 화면 클릭시 User 착수 현상 발견 (미해결)
       버그 3. 승리, 패배화면 이미지 변경시 프로그램 멈춤현상 발생 (해결)
     
    * 업무 분배파트 재설정
     모든 팀원 오픈소스 Class 별 해석 진행

### 오파고 프로젝트 전개
* main.py에서 파이게임(오목) 시작
** 최초 시작 시 AI 최초 착수 위치는 rand(x,y)값을 Random.Range 함수를 이용하여 공통 8~12 좌표의 위치 중 임의의 위치에 착수
```
rand_x or rand_y = random.randrange(8,12)
```


## 정보
* License : http://github.com/NamHoKi/AI-Omok



