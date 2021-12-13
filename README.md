# Project : Team-Ace 오파고

## 프로젝트 개요
> * 오목 AI 게임 오픈소스를 활용하여 내부 알고리즘을 이해하고 본 강의에서 배운 내용을 접목시켜 프로그래밍에 대한 폭넓은 이해와 팀워크를 배움에 목적을 둔 프로젝트<br/>
> * End Cheak Point로 승리 또는 패배 결과 도출
> * AI는 자신의 차례에서 가장 가중치가 높다고 판단하는 위치에 착수하도록 유도함
> * License : http://github.com/NamHoKi/AI-Omok

## 개발 환경
> * [Python Version] : 3.10<br/>
> * [Encoding] : UTF-8

## 사용된 기술
> * Artificial Intelligence, AI
> * DataBase, DB
> * Graphical User Interface, GUI - Pygame
> ```ps
> pip install pygame
> ```

## 팀 소개(ACE)
> 번호 | 이름 | 역할 |
> --- | --- | --- |
> 1 | 서숭용 | - |
> 2 | 허찬 | - |
> 3 | 송환욱 | - |
> 4 | 박종광 | - |
> 5 | 문아영 | - |
> 6 | 김동현 | Leader |
> 7 | 강민기 | - |
> 8 | 김하민 | - |
> 9 | 유태우 | - |
> * * *

# 프로젝트 전개

## Rule
> - 승리 조건 : 5목 이상(6목, 7목 등)
> - 시간제한 : 없음
> - AI : 흑(先) | User : 백(後)
> - 3 x 3 : 흑, 백 모두 금지
> - 4 x 4 : 흑, 백 모두 가능

## Start
> ### 오픈소스의 전개
> 1. 흑(AI)이 먼저 돌을 놓습니다.
> 2. 이후 백(User)이 놓을 위치를 선택합니다.
> 3. 승리 or 패배 조건을 만족하면 5초 뒤 재시작합니다.
> 
> ### 구현하려던 전개
> 1. 시작 버튼을 누르면 흑(AI)이 먼저 돌을 놓습니다.<br/>
> 2. 이후 백(User)이 놓을 위치를 선택합니다.<br/>
> 3-1-1. 백(User)의 승리 시, 승리 화면으로 넘어갑니다.<br/>
> 3-1-2. 승리자의 이름을 입력합니다.<br/>
> 3-1-3. 승리자의 이름을 입력을 하면 기록과 함께 순위표가 생성됩니다.<br/>
> 3-1-4. 승리하면 재시작 버튼을 통해 재시작을 할 수 있습니다.<br/>
> 3-2. 백(User)가 패배하면 재시작 버튼을 통해 재시작 합니다.<br/>

## 구현하고자 했던 기능
> * 시작 버튼을 통한 게임 시작
> * 시작과 동시에 게임이 종료될 때까지 시간 측정
>   * 최소 시간 승리 랭킹 구현
> * 졌을 경우 재도전 버튼을 통해 게임 재시작
> * 이겼을 경우 승리 화면 생성
>   * 승리 화면 이름 입력칸 생성
>   * 이름 입력 시 승리한 판에 대한 승리 시간 저장
> * 저장된 기록들을 짧은 시간순으로 랭킹 표출

## 업데이트 & 개선한 점
> * 0.1.0(21/11/05)
>     * 최종엔.exe을 사용하여 프로젝트를 완성하려고 했으나, 위험성이 높다는 교수님의 의견으로.exe는 사용 배제 및 삭제
>     * 오픈소스의.Py파일들을 Main.py로 병합 후 PowerShell 터미널에서 실행 가능하도록 함(파일 간편화)
>
> * 0.1.3(21/11/11)
>     * 승리, 패배 화면 Mockup 파일 제작 및 적용
>     * PowerShell에서 프로그램 이용 시 간헐적 오류였던 병합 형태에서의 temp x, y 변수 로컬 지정으로 인한 오류 발생(개선 방법 : temp_x, teem_y의 값을 글로벌화 시킨 뒤 지정 초기화)
> ```
> PS C:\Users\SONG\Desktop\Team-Ace\Ace_Project> py main.py
> pygame 2.1.0 (SDL 2.0.16, Python 3.10.0)
> Traceback (most recent call last):
>   File "C:\Users\SONG\Desktop\Team-Ace\Ace_Project\main.py", line 137, in <module>
>     main.start()
>   File "C:\Users\SONG\Desktop\Team-Ace\Ace_Project\main.py", line 116, in start
>     if temp_x <= 420 and temp_y <= 420:
> UnboundLocalError: local variable 'temp_x' referenced before assignment
> ```
>
> * 0.1.8(21/11/18)
>     * [GUI]Pygame 개념 학습
>     * [DB]MYSQL, SQLITE 개념 학습
>
> * 0.2.0(21/11/25)
>     * 오목 Game, pygame으로 구동 시작 및 버그 관련 정보 탐색
>        버그 1. 최상단, 최좌측 백(User) 돌 착수 불가능(미해결)
>        버그 2. 게임 승리 및 패배 화면 카운트 중 오목판 화면 클릭 시 백(User) 돌이 착수되는 현상(미해결)
>        버그 3. 승리 또는 패배 화면 이미지 변경 시 프로그램 멈춤 현상(해결)
>     * 업무 분배 재설정
>        모든 팀원 오픈소스 Class 별 해석 진행

## 스크린샷
> * 실행화면<br/>
> ![omok](https://user-images.githubusercontent.com/48282708/71707199-feb57e00-2e2b-11ea-9257-977c33195025.png)
> * 승리화면<br/>
> ![최최종 승리](https://user-images.githubusercontent.com/89123613/143179363-44e6a02e-4132-443f-b6a4-7f405b6ebd02.JPG)
> * 순위등록화면<br/>
> ![승리후 순위등록](https://user-images.githubusercontent.com/89123604/141059817-fbe566d5-929e-4fb2-a435-f4bd4c618e12.JPG)
> * 순위화면<br/>
> ![랭킹 최종](https://user-images.githubusercontent.com/89123613/143179355-5aad8886-dcfb-4e8b-bd62-77642749e66b.JPG)
> * 패배화면<br/>
> ![최최종 패배](https://user-images.githubusercontent.com/89123613/143179370-b3af6739-595d-4e64-8b77-932bb8e843f9.JPG)
> * * *

# 결론

## 개선할 점
> * 재시작 전 카운트 다운할 때, 마우스 이벤트 오류 수정
> * MinMax 알고리즘을 사용하여 더 많은 수 예측
> * 4x3 or 4x4를 할 때, 띄워진 4를 3으로 인식해서 3x3으로 잘못 인식
> * 카운트다운 할 때, quit 이벤트 안 먹힘
> * 최좌측, 최상단 백(User)의 돌 착수 불가 현상
 
## 이 프로젝트가 유용했던 이유
> * 문제해결능력 향상
> * Python의 기본 스킬 향상
> * 팀 협업의 전개 및 중요성, 의사소통능력 향상
> * 프로그래밍, 코딩에 대한 두려움 극복

## 팀 전체 후기
> 　우리가 게임이라는 장르를 선택한 이유는 많은 조원들이 관심을 가질 수 있는 공통 분야에 대한 고민에서 게임이라는 장르를 선택하게 되었다.
> 특히 우리 조가 선택한 AI 오목 게임은 타 게임에 비해 교과과정에서 배운 기술들과 유사성이 짙고 접해보지 못한 종목이라 흥미로웠다.
> 해당 게임의 오픈소스에서 추가로 구현하고자 했던 기능들은 데이터베이스를 기반으로 한 랭킹 시스템, 승패 화면 전환 기능, Scene 및 Button 추가로 기존보다 완성도 높은 게임을 만들고자 했다.
> 주로 Pygame의 전개 이해, Board 내의 흑/백 착수 유무 판단에 각각 부여되는 가중치 부분을 확인 및 해석하기 위해 디버깅이나, 가중치 표출 코딩 등을 시도했었다.<br/>
>
> 　하지만 예상보다 부족했던 시간과 높은 수준의 난이도로 인해 우리들이 원하는 목표치에 도달하지 못하여 아쉬웠다.
> 이미 완성되어 있는 코드들의 해석이 우선이었기 때문에 이 부분에서 공부하며 많은 시간을 소모하게 됐는데, 이로 인해 개선하려고 했던 부분과 기획했던 변경 사항들은 이루어내지 못했다.<br/>
>
> 　그래도 이런 문제점들을 해결하면서 전체적인 코딩 및 프로그래밍에 대한 이해도가 높아졌다.
> 또 코딩에 대한 팀 프로젝트를 하며 역할 분배의 문제를 인식하고 개선하는 등 전반적으로 팀 활동에 대한 경험치를 쌓을 수 있었다.
> 다소 어려운 문제와 익숙지 않은 프로젝트라는 과제 형식에 많은 난관이 있었으나 이따금 개개인의 노력으로 잘 해결해 나갈 수 있었던 것 같다.
> 어려운 오픈소스 코드를 해석함에 있어 집단지성의 힘으로 가설을 세우고 그 가설이 참으로 증명될 때의 희열과 성취감을 느낄 수 있었다.
> 이렇듯 팀 프로젝트라는 과제를 수행함에 있어 최초의 목표에 다가가진 못했지만 혼자라면 하지 못했을 문제들을 함께여서 해결할 수 있었던 것 같다.
> * * *
