import pygame

WHITE = (255,255,255)
pad_width = 1024
pad_height = 512
background_width = 1024

def back(background,x,y):
    global gamepad
    gamepad.blit(background,(x,y))

def click(x,y):
    global gamepad, aircraft
    gamepad.blit(aircraft,(x,y))

def runGame():
    global gamepad, clock ,aircraft ,background1 ,background2

    x = pad_width * 0.01
    y = pad_height * 0.75
    y_change = 0

    background1_x = 0
    background2_x = background_width

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
                        y_change =0


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        y_change =0

        y += y_change
        x += x_change

        gamepad.fill(WHITE)

        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width


        back(background1,background1_x, 0)
        back(background2,background2_x, 0)

        click(x,y)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def initGame():
    global gamepad, clock , aircraft ,background1,background2

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('batting game')
    aircraft = pygame.image.load('images/click.jpg')
    background1 = pygame.image.load('images/background.jpg')
    background2 = background1.copy()


    clock = pygame.time.Clock()
    runGame()

if __name__ =='__main__':
    initGame()