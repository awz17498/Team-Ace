import pygame ## 파이게임 생성
pygame.init()

BLACK = (   0,   0,   0)
WHITE = (255,  255, 255)
BLUE  = (   0,   0, 255)
GREEN = (   0, 255,   0)
RED   = (255,   0,    0)


screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("허찬의 테스트")

done = False

clock = pygame.time.Clock()


while not done:
    
    clock.tick(10) ##초당 FPS(프레임)을 설정 값이 10인경우 초당 10번의 화면을 출력
                    ##높으면 높을수록 cpu소모 과다

    ####메인루프###
    for event in pygame.event.get():  ##함수를 통해 게임 중간에 발생한 이벤트를 캐치 및 검사,
        if event.type == pygame.QUIT:  ##함수를 통해 가져온 이벤트가 만약 QUIT와 일치하는지 검사
            done=True ##만약 맞다면 while문이 더이상 돌아가지 않도록 바꿔줍니다.
        
        
    screen.fill(WHITE)
    
    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 5) ## 삼각형
    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 0) ##삼각형
    pygame.draw.lines(screen, RED, False, [[50,150], [50, 250], [200, 250], [200, 150]], 5) ##여러개의 선
    pygame.draw.rect(screen, BLACK, [75, 175, 75, 50], 5) ## 사각형
    pygame.draw.rect(screen, BLUE, [75, 175, 75, 50], 0) ## 사각형
    pygame.draw.line(screen, BLACK, [112, 175], [112, 225], 5) ## 선
    pygame.draw.line(screen, BLACK, [75, 200], [150, 200], 5) ## 선
    
    
    pygame.display.flip()
    
    
pygame.quit()



