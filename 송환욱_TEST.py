import pygame

class Start_Ace_Omok(object):
    def start(self):
        # Pygame 초기화
        pygame.init()

        # 프로그램 넓이, 높이
        Start_Screen_Width = 400
        Start_Screen_Height = 300

        # Start_Screen 생성
        Start_Screen = pygame.display.set_mode((Start_Screen_Width, Start_Screen_Height))

        # Start_Screen 타이틀 설정
        pygame.display.set_caption("Ace_Start_Screen")

        # 게임 루프
        playing = True

        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    pygame.quit()

                # 색상 상수
                White = (255, 255, 255)

                # 스크린 배경색 칠하기
                Start_Screen.fill((0, 0, 0))

                # Font 객체 생성
                myFont = pygame.font.SysFont("arial", 30, True, False)

                # Text를 surface에 그리기("내용", 안티앨리어싱, "검은색")
                text_Title= myFont.render("Press 'Spacebar' to Start", True, White)

                # Rect 생성
                text_Rect = text_Title.get_rect()

                # 가로, 세로 가운데
                text_Rect.centerx = round(Start_Screen_Width / 2)
                text_Rect.centery = round(Start_Screen_Height / 2)

                # Text Surface SCREEN에 복사하기, Rect 사용
                Start_Screen.blit(text_Title, text_Rect)

                # 작업한 스크린의 내용을 갱신하기
                pygame.display.flip()

                # 스페이스바 키가 눌렸을 때
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("스페이스바 키 눌림")