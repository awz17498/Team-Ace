import pygame
 
# 전체 스크린의 가로, 세로 크기 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
 
# 초기화
pygame.init()
 
# 스크린 생성
SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
 
# window의 타이틀 설정
pygame.display.set_caption("pygame test")
 
myRect = pygame.Rect(150, 200, 200, 100)

print("myRect = ", myRect)
print("myRect.x = ", myRect.x)
print("myRect.y = ", myRect.y)
print("myRect.w = ", myRect.w)
print("myRect.h = ", myRect.h)
print("myRect.width = ", myRect.width)
print("myRect.height = ", myRect.height)
print("myRect.left = ", myRect.left)
print("myRect.right = ", myRect.right)
print("myRect.top = ", myRect.top)
print("myRect.bottom = ", myRect.bottom)
print("myRect.centerx = ", myRect.centerx)
print("myRect.centery = ", myRect.centery)
print("myRect.size = ", myRect.size)
print("myRect.topleft = ", myRect.topleft)
print("myRect.topright = ", myRect.topright)
print("myRect.bottomleft = ", myRect.bottomleft)
print("myRect.bottomright = ", myRect.bottomright)
print("myRect.midleft = ", myRect.midleft)
print("myRect.midright = ", myRect.midright)
print("myRect.midtop = ", myRect.midtop)
print("myRect.midbottom = ", myRect.midbottom)