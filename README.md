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

# Project : 오파고
#### 기획 내용
오목 AI게임 오픈소스를 활용하여 내부 알고리즘을 이해하고 본 강의에서 배운 내용을 접목 시켜 프로그래밍에 대한 폭넓은 이해와 팀워크를 배움에 목적을 둔 프로젝트 입니다.
* 적용 기술
  * DB
  * GUI
  * AI

# 송환욱
#### ~~※오목1 예제 실험~~
~~1. 최초 실행시 오류 : import numpy 에러(numpy package가 설치되어 있지 않기 때문)~~
~~2. 터미널에서 numpy Package 존재여부 체크~~
```python
pip show numpy
```
~~3. numpy Package 설치~~
```python
pip install numpy
```
~~4. 실행 결과 : **GUI가 아닌** 응용 프로그램 내에서 실행됐음~~

~~p.s 넘파이 체크도 안된다면 파이썬 재설치하면 해결~~

#### ※오목2 예제 실험
1. pygame 설치
```python
pip install pygame
```
2. 내부 폴더에(\Omok_Project\dist\AI_오목\AI오목.exe)을 실행하면 구동됨

2. pyinstaller 설치(https://shgl.tistory.com/21)
```python
pip install pyinstaller
```
#### ※py(스크립트)파일을 exe(실행파일)로 변환하는 작업
[https://kkamikoon.tistory.com/129]
콘솔창이 출력되지 않게 하려면 아래와 같이 명령어에 '-w' 또는 '--windowed'를 추가해줍니다.
```ps
pyinstaller -w 
```
#### 앞으로 해야할 일
1. pygame 모듈에 대한 공부
[https://kkamikoon.tistory.com/129]



------------
------------
------------
# 오목 예제 2 리드미 백업
# AI-Omok Mini Project
------------
## Project info
##### - 오목판의 흐름을 스스로 판단하여 두는 AI를 만드는 것이 목표입니다.
##### - 학습이나 다음 수를 예상하는 것이 아닌 자신의 차례에서 가장 가치있는 곳에 돌을 둡니다.
##### - 오목판의 흐름을 판단할 때, 저의 주관적인 영향이 있을 수 있습니다.
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
##### 1. 시작하면 흑(AI)이 먼저 돌을 놓습니다.
##### 2. 마우스로 백(User)이 놓을 곳을 선택합니다.
##### 3. 승리조건을 만족하면 5초 뒤 재시작합니다.

------------
## ScreenShot
![omok](https://user-images.githubusercontent.com/48282708/71707199-feb57e00-2e2b-11ea-9257-977c33195025.png)
------------
## Step
##### 1. 콘솔을 목표로 기본적인 코딩
##### 2. GUI
##### 3. 오류 수정 및 첫 시제품 완성
##### 4. 충분한 테스팅을 통한 코드 개선 및 수정
------------
## Memo
### 어려웠던 점
##### 1. 처음 사용해보는 Python GUI의 어려움
##### 2. 오목판의 흐름을 판단할 방법
##### - 모든 좌표의 가중치(ex : 승리조건을 만족하는 곳이면 큰 수)를 계산하여 가장 높은 가중치의 좌표를 두게함
![o1](https://user-images.githubusercontent.com/48282708/73593289-b8942d00-4545-11ea-886e-45d81ec643ad.png)
##### - 패턴을 미리 정해놓고 체크하며 가중치 계산
### 개선할 점
##### 1. 재시작 전 카운트 다운할 때, 마우스 이벤트 오류 수정
##### 2. MinMax 알고리즘을 사용하여 더 많은 수 예측
