import random
import time
import sys
import pygame
from pygame.locals import *

class Main(object):
    def start(self):
        pygame.init() # pygame 초기화
        screen = pygame.display.set_mode((770, 420)) # 프로그램 해상도 설정
        pygame.display.set_caption("ACE_오파고") # 파이게임 제목 설정

        board = Board()
        ai = AI("AI", "○")
        rule = Rule()
        turn = True # AI 차례 = False / user 차례 = True
        count = 1
        
        temp_x = 0
        temp_y = 0

        rand_x = random.randrange(8, 12) # 8 이상 12 미만의 난수 중 하나를 무작위로 얻음(X좌표)
        rand_x = rand_x * 21 + 10 # (8 x 21 + 10 = 178), (9 x 21 + 10 = 199), (10 x 21 + 10 = 220), (11 x 21 + 10 = 241) 무작위로 나올 수 있는 난수들을 공식에 대입한 값

        rand_y = random.randrange(8, 12) # 8 이상 12 미만의 난수 중 하나를 무작위로 얻음(Y좌표)
        rand_y = rand_y * 21 + 10 # (8 x 21 + 10 = 178), (9 x 21 + 10 = 199), (10 x 21 + 10 = 220), (11 x 21 + 10 = 241) 무작위로 나올 수 있는 난수들을 공식에 대입한 값

        black_stones = [[rand_x, rand_y]]  # 난수가 8 ~ 12 인 이유는 바둑판 20 x 20 의 중앙에서 시작하게끔 설정.
        white_stones = []

        end_check = False # 최초 실행 시 승리 판정을 False로 하여 진행 가능

        while True:
            user_select_x = False
            user_select_y = False
            three_x_three_warning = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                LEFT = 1 # 왼쪽 버튼에 대한 버튼 인덱스

                # 좌클릭시 놓아지는 부분
                if event.type == MOUSEBUTTONUP and event.button == LEFT: # 마우스 버튼을 누른 후 뗄 때 발생함 + 마우스 좌클릭(AND)
                    '''
                    pygame.mouse.get_pos()
                    마우스의 포지션 x, y 값을 튜플로 반환한다.
                    pygame.mouse.get_pos() -> (123, 345)
                    '''
                    mouse_xy = pygame.mouse.get_pos()
                    '''
                    소수점 이하의 수를 모두 버리고 몫만 나타낼 때 ‘//’ 연산자를 사용
                    ''' 
                    print(pygame.mouse.get_pos())
                    x = (mouse_xy[0] - 10) // 21 # 미해석
                    y = (mouse_xy[1] - 10) // 21 # 미해석
                    user_select_x = y # 미해석
                    user_select_y = x # 미해석

                # 커서가 안내하는 부분
                elif event.type == MOUSEMOTION: # 마우스가 움직일 때 발생함
                    mouse_xy = pygame.mouse.get_pos()
                    x = (mouse_xy[0] - 10) // 21 # 미해석
                    y = (mouse_xy[1] - 10) // 21 # 미해석
                    temp_x = x * 21 + 10 # 미해석
                    temp_y = y * 21 + 10 # 미해석

            # 게임의 상태를 업데이트하는 부분
            if turn == False: # AI의 턴일 때
                x, y = ai.select_stone(board)
                gui_x = y * 21 + 10  ## 21: 바둑알의 크기 10: 바둑판 라인의 거리
                gui_y = x * 21 + 10  ## 21: 바둑알의 크기 10: 바둑판 라인의 거리
                board.put_stone(x, y, 11) ## 11은 black 의 번호. 즉 좌표에 AI가 놓았다는걸 확인
                black_stones.append([gui_x,gui_y])
                if rule.win_check(x, y, board, 11):
                    end_check = 'black' # AI의 승리
                count += 1
                turn = not turn
            else:
                if user_select_x and user_select_y:
                    x, y = user_select_x, user_select_y
                    gui_x = y * 21 + 10 ## 21: 바둑알의 크기 10: 바둑판 라인의 거리
                    gui_y = x * 21 + 10 ## 21: 바둑알의 크기 10: 바둑판 라인의 거리
                    if rule.stone_check(x, y, board):
                        if rule.three_x_three_check(x, y, board, 10):
                            white_stones.append([gui_x, gui_y])
                            board.put_stone(x, y, 10)
                            if rule.win_check(x, y, board, 10):
                                end_check = 'white' # User의 승리
                            count += 1
                            turn = not turn
                        else:
                            three_x_three_warning = True

            # 게임의 상태를 화면에 그려주는 부분 -> 화면을 지우고 업데이트하는 코드
            screen.fill((255, 255, 255)) # 공백 RGB 지정
            screen.blit(pygame.image.load('Image/omok_board.jpg'), (0, 0)) # '오목판'IMG 출력
            screen.blit(pygame.image.load('Image/rule.jpg'), (420, 0)) # '룰'IMG 출력

            for st in white_stones: # 백돌 RGB, SIZE 지정
                pygame.draw.circle(screen, (250, 250, 250), st, 10)

            for st in black_stones: # 흑돌 RGB, SIZE 지정
                pygame.draw.circle(screen, (0, 0, 0), st, 10)

            pygame.draw.circle(screen,(120,120,120),black_stones[-1], 10) # 마지막 흑돌 RGB, SIZE 지정

            if three_x_three_warning: # 3x3 경고 트리거
                screen.blit(pygame.image.load('Image/33.jpg'),(200, 100)) # '3x3 경고'IMG 출력
                pygame.display.update()
                time.sleep(1) # 타이머 1초

            if temp_x <= 420 and temp_y <= 420: # 마우스의 좌표가 오목 판 내에 있을 때 / 착수 전 백돌 RGB와 SIZE 지정
                pygame.draw.circle(screen, (220, 220, 220),[temp_x,temp_y], 10)

            if end_check == 'black': # 만약 AI의 승리 판정일 때
                for i in range(5, 0, -1):
                    screen.blit(pygame.image.load('Image/ai'+str(i)+'.jpg'), (465, 55)) # Image폴더의 ai1/2/3/4/5를 문자열에서 정수형으로 변환함
                    pygame.display.update()
                    time.sleep(1) # 이미지 사진을 1초 딜레이 주어 표현(총 5장 = 5초)

            elif end_check == 'white': # 만약 유저의 승리 판정일 때
                for i in range(5, 0, -1):
                    screen.blit(pygame.image.load('Image/user'+str(i)+'.jpg'),(465, 55)) # Image폴더의 user1/2/3/4/5를 문자열에서 정수형으로 변환함
                    pygame.display.update()
                    time.sleep(1) # 이미지 사진을 1초 딜레이 주어 표현(총 5장 = 5초)
            else:
                pygame.display.update()

            if end_check:
                self.start()
            '''
            AI가 승리하면 재시작
            if end_check == black:
            self.start()
            '''

class Board(object):
    def __init__(self): # 오목판
        self.omok_board = [[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],  "그냥 숫자"
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
                           [7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9]]
                           
    def put_stone(self, x, y, color):
        # 오목판에 돌을 둡니다.
         # :param x: int - 오목판 x좌표
         # :param y: int - 오목판 y좌표
         # :param color: int - (x,y) 좌표의 color - 10(백) or 11(흑)
         # :return:
        self.omok_board[x][y] = color

class Offset(object):
    def __init__(self): # 3시부터 시계 방향으로 8방향
        self.offset = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

class Rule(Offset):
    def __init__(self):
        super().__init__()

    def stone_check(self, x, y , board):
        '''
        원래 돌이 있는 자리인지, 좌표값 밖인지 체크합니다.
        
        :param x: int - 확인할 x좌표
        :param y: int - 확인할 y좌표
        :param board: Board - 오목판
        :return: bool - 둘 수 없으면 False, 둘 수 있으면 True
        '''
        if x < 0 or x >= len(board.omok_board) or y < 0 or y >= len(board.omok_board):
            # x가 0보다 작을 때
            # x가 len(board.omok_board)요소의 전체 개수보다 크거나 같을 때
            # y가 0보다 작을 때
            # y가 len(board.omok_board)요소의 전체 개수보다 크거나 같을 때
            return False
        elif board.omok_board[x][y] == 11 or board.omok_board[x][y] == 10:
            # 11(흑)
            # 10(백)
            return False
        else:
            return True

    def three_x_three_check(self, x, y , board , color):
        '''
        3x3을 체크합니다.

        :param x: int - 확인할 x좌표
        :param y: int - 확인할 y좌표
        :param board: Board - 오목판
        :param color: int - 10 : 백 / 11 : 흑
        :return: bool - 3x3이면 False , 아니면 True
        '''
        b = board.omok_board
        o = self.offset
        three_count = 0
        three_way =  ['011100','001110','010110','011010'] # 3이 될수 있는 경우

        # 양방향으로 체크할것이기 때문에 for문은 4방향.
        for i in range(4):
            check_pattern = '1'
            x_check = x
            y_check = y
            for j in range(4):
                x_check += o[i][0]
                y_check += o[i][1]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                    break

                check_xy = b[x_check][y_check]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                        break
                if check_xy == color:
                    check_pattern = '1' + check_pattern
                elif check_xy < 10:
                    check_pattern = '0' + check_pattern
                else:
                    break
            x_check = x
            y_check = y
            for j in range(4):
                x_check -= o[i][0]
                y_check -= o[i][1]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                    break

                check_xy = b[x_check][y_check]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                        break
                if check_xy == color:
                    check_pattern = check_pattern + '1'
                elif check_xy < 10:
                    check_pattern = check_pattern + '0'
                else:
                    break

            for three_list in three_way:
                if three_list in check_pattern:
                    three_count+=1
                    break

        if three_count >= 2:
            return False

        return True

    def win_check(self, x, y , board, color):
        '''
        오목, 장목을 두었는지 확인하는 함수입니다.
        오목을 넘는 장목도 승리로 판단합니다.
        :param x: int - 방금 둔 수의 x좌표
        :param y: int - 방금 둔 수의 y좌표
        :param board: 오목 board
        :param color: int - 방금 둔 수의 색 10 : 백 , 11 : 흑
        :return: bool - True : 승리조건 만족 , False : 승리조건 불만족
        '''
        b = board.omok_board
        o = self.offset
        check_count = [1] * 8

        for i in range(8):
            x_check = x + o[i][0]
            y_check = y + o[i][1]
            while True:
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b) or b[x_check][y_check] != color:
                    break
                else:
                    if b[x_check][y_check] == color:
                        check_count[i] += 1
                        x_check = x_check + o[i][0]
                        y_check = y_check + o[i][1]
                    else:
                        break

        for i in range(4):
            if check_count[i] + check_count[i+4] -1 >= 5:
                return True

        return False

class AI(Offset):
    def __init__(self, nick_name, color):
        '''
        :param nick_name: string
        :param color: string
        '''
        super().__init__()
        self.nick_name = nick_name
        self.color = color

    def select_stone(self,board):
        '''
        self.AI_select_stone 을 호출하고 반환합니다.
        :param board: Board - 오목판
        :return: list - 최선의 수라고 판단 된 (x,y)좌표
        '''
        return self.AI_select_stone(board)

    def AI_select_stone(self,board):
        '''
        AI가 모든 좌표의 가중치 값중 가장 높은 값을 선택합니다.
        :param board: Board - 오목판
        :return: list - 최선의 수라고 판단 된 (x,y)좌표
        '''
        ai_max_weight = 0
        user_max_weight = 0
        max_weight = 0

        for i in range(20):
            for j in range(20):
                ai_weight = self.analysis_pattern(i,j,board,11)
                user_weight = self.analysis_pattern(i,j,board,10)

                if ai_weight >= 10000:
                    return i,j
                elif user_weight >= 10000 and ai_weight != -1:
                    user_weight = 10000

                if max_weight < ai_weight + user_weight and ai_weight != -1:
                    max_weight = ai_weight + user_weight
                    max_xy = [i,j]

                if ai_max_weight < ai_weight and ai_weight != -1:
                    ai_max_weight = ai_weight
                    ai_xy = [i,j]

                if user_max_weight < user_weight:
                    user_max_weight = user_weight

        if ai_max_weight >= user_max_weight:
            return ai_xy
        else:
            return max_xy

    def analysis_pattern(self, x, y , board , color):
        '''
        오목판의 (x,y)좌표의 가중치를 계산하여 반환합니다.
        :param x: int - x좌표
        :param y: int - y좌표
        :param board: Board - 오목판
        :param color: int - 10 : 백 / 11 : 흑
        :return: int - 가중치
        '''
        b = board.omok_board
        o = self.offset

        if b[x][y] >= 10:
            return -1

        two_1 = ['001010','010100','010010']
        two_2 = ['01100', '00110']
        three_6 = ['010110', '011010']
        three_8 = '01110'
        four_8 = ['10111','11011','11101']
        four_10 = ['11110','01111']
        four_50 =  '011110'

        weight = 0
        three_count = 0
        four_count = 0

        # 양방향으로 체크할것이기 때문에 for문은 4방향.
        for i in range(4):
            check_pattern = '1'
            x_check = x
            y_check = y
            for j in range(4):
                x_check += o[i][0]
                y_check += o[i][1]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                    break

                check_xy = b[x_check][y_check]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                        break
                if check_xy == color:
                    check_pattern = '1' + check_pattern
                elif check_xy < 10:
                    check_pattern = '0' + check_pattern
                else:
                    break
            x_check = x
            y_check = y
            for j in range(4):
                x_check -= o[i][0]
                y_check -= o[i][1]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                    break

                check_xy = b[x_check][y_check]
                if x_check < 0 or x_check >= len(b) or y_check < 0 or y_check >= len(b):
                        break
                if check_xy == color:
                    check_pattern = check_pattern + '1'
                elif check_xy < 10:
                    check_pattern = check_pattern + '0'
                else:
                    break

            for three in three_6:
                if three in check_pattern and (not ('11101' in check_pattern)) and (not ('10111' in check_pattern)):
                    weight += 6
                    three_count += 1
                    if three_count == 2:
                        return -1

            if three_8 in check_pattern and (not ('11101' in check_pattern)) and (not ('10111' in check_pattern)):
                weight += 8
                three_count += 1
                if three_count == 2:
                    return -1

            if '11111' in check_pattern:
                return 10000

            if four_50 in check_pattern:
                weight += 50

            for two in two_1:
                if two in check_pattern:
                    weight += 1

            for two in two_2:
                if two in check_pattern:
                    weight += 2

            for four in four_8:
                if four in check_pattern:
                    weight += 8
                    four_count += 1
                    if four_count + three_count > 1:
                        weight += 150

            for four in four_10:
                if four in check_pattern:
                    weight += 10
                    four_count += 1
                    if four_count + three_count > 1:
                        weight += 150
        return weight

if __name__ == "__main__":
    Start = Main()
    Start.start()