import sys
import time
import pygame
import random

pygame.init()

white = (255, 255 ,255)

titleIMG = pygame.image.load('images/title.png')
startIMG = pygame.image.load('images/starticon.png')
quitIMG = pygame.image.load('images/quiticon.png')
clickStartIMG = pygame.image.load('images/clickedStartIcon.png')
clickQuitIMG = pygame.image.load('images/clickedQuitIcon.png')


display_width = 800
display_height = 400
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('베인의 모험')

clock = pygame.time.Clock()

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act,y_act,action =None):
        mouse = pygame.mouse.get_pos() #마우스 좌표 저장
        click = pygame.mouse.get_pressed() #클릭시
        if x + width > mouse[0] > x and y + height > mouse[1] > y: #이미지 안에 있으면
            gameDisplay.blit(img_act,(x_act, y_act)) #클릭 이미지 로드
            if click[0] and action != None:
                time.sleep(1)                  # 1초동안 지연
                action()                       # 지정함수 호출
        else:
            gameDisplay.blit(img_in,(x,y))         #마우스가 이미지 바깥이면 일반 이미지 로드


def quitgame():
    pygame.quit()
    sys.exit()



def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)

        titletext = gameDisplay.blit(titleIMG, (100,50))
        startButton = Button(startIMG,280,260,60,20,clickStartIMG,273,258,selectScreen)
        quitButton = Button(quitIMG,445,260,60,20,clickQuitIMG,440,258,quitgame)
        pygame.display.update()
        clock.tick(15)

def selectScreen():
    WHITE = (255, 255, 255)
    pad_width = 1024
    pad_height = 512
    background_width = 1024

    def drawObject(obj, x, y):
        global gamepad
        gamepad.blit(obj, (x, y))

    # def back(background,x,y):
    #    global gamepad
    #    gamepad.blit(background,(x,y))

    # def click(x,y):
    #    global gamepad, aircraft
    #    gamepad.blit(aircraft,(x,y))

    def runGame():
        global gamepad, clock, aircraft, background1, background2
        global poro, temos

        x = pad_width * 0.01
        y = pad_height * 0.75
        y_change = 0

        background1_x = 0
        background2_x = background_width

        poro_x = pad_width
        poro_y = random.randrange(0, pad_height)

        temo_x = pad_width
        temo_y = random.randrange(0, pad_height)
        random.shuffle(temos)
        temo = temos[0]

        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -5
                    elif event.key == pygame.K_DOWN:
                        y_change = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0

            y += y_change
            gamepad.fill(WHITE)

            background1_x -= 2
            background2_x -= 2

            poro_x -= 7
            if poro_x <= 0:
                poro_x = pad_width
                poro_y = random.randrange(0, pad_height)

            if temo == None:
                temo_x -= 30
            else:
                temo_x -= 15

            if temo_x <= 0:
                temo_x = pad_width
                temo_y = random.randrange(0, pad_height)
                random.shuffle(temos)
                temo = temos[0]

            if background1_x == -background_width:
                background1_x = background_width

            if background2_x == -background_width:
                background2_x = background_width

            drawObject(background1, background1_x, 0)
            drawObject(background2, background2_x, 0)
            drawObject(poro, poro_x, poro_y)
            if temo != None:
                drawObject(temo, temo_x, temo_y)
            drawObject(aircraft, x, y)

            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()

    def initGame():
        global gamepad, clock, aircraft, background1, background2
        global poro, temos

        temos = []

        pygame.init()
        gamepad = pygame.display.set_mode((pad_width, pad_height))
        pygame.display.set_caption('베인의 모험')
        aircraft = pygame.image.load('images/click.png')
        background1 = pygame.image.load('images/background.png')
        background2 = background1.copy()
        poro = pygame.image.load('images/poro.png')
        temos.append(pygame.image.load('images/temo1.png'))
        temos.append(pygame.image.load('images/temo2.png'))

        for i in range(5):
            temos.append(None)

        clock = pygame.time.Clock()
        runGame()

    if __name__ == '__main__':
        initGame()

mainmenu()
game_loop()