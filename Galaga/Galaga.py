#better random movement on enemies
#highscore method









import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
ship = pygame.image.load('Gship.png')
ship = pygame.transform.scale(ship, (50, 50))
beam = pygame.image.load('beam.png')
beam = pygame.transform.scale(beam, (10, 30))
badguy = pygame.image.load('spaceEnemy.png')
badguy = pygame.transform.scale(badguy, (50, 50))
badguy2 = pygame.image.load('spaceEnemyBlue.png')
badguy2 = pygame.transform.scale(badguy2, (50, 50))
badguy3 = pygame.image.load('spaceEnemyRed.png')
badguy3 = pygame.transform.scale(badguy3, (50, 50))
badguy4 = pygame.image.load('spaceEnemyYellow.png')
badguy4 = pygame.transform.scale(badguy4, (50, 50))
badguy5 = pygame.image.load('spaceEnemyBlack.png')
badguy5 = pygame.transform.scale(badguy5, (50, 50))
back = pygame.image.load('spaceBack.jpeg')
back = pygame.transform.scale(back, (800, 600))


def crash(points):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()
                if event.key == pygame.K_ESCAPE:
                    quit()
        screen.blit(back, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 105)
        smallText = pygame.font.Font('freesansbold.ttf', 35)
        TextSurf, TextRect = text_objs("You Lose!", largeText, white)
        TextSurf2, TextRect2 = text_objs("Final Score: " + str(points) + "", smallText, white)
        TextRect2.center = (130 , 20)
        TextRect.center = (display_width * 0.5 , display_height * 0.5)
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf, TextRect)
        button("Play Again?", 150, 450, 100, 50, green, bright_green, game_intro)
        button("Quit!", 550, 450, 100, 50, red, bright_red, "quit")


        pygame.display.update()
        clock.tick(15)

def timer(seconds):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Time Remaining: " + str(seconds), True, white)
    screen.blit(text,(630,0))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objs(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def score(points):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Points: " + str(points), True, white)
    screen.blit(text,(0,0))

def dif(points):
    font = pygame.font.SysFont(None, 25)
    if points >= 10:
        text = font.render("Difficulty: Medium", True, white)
        if points >= 20:
            text = font.render("Difficulty: Hard", True, white)
            if points >= 30:
                text = font.render("Difficulty: Ultra", True, white)
    else:
        text = font.render("Difficulty: Easy", True, white)

    screen.blit(text,(625,0))


def text_objs(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objs(text, largeText)
    TextRect.center = (800 * 0.5 , 600 * 0.5)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game()

def enemy(ex, ey, points):
    if points >= 40:
        screen.blit(badguy5, (ex, ey))
    elif points >= 30:
        screen.blit(badguy4, (ex, ey))
    elif points >= 20:
        screen.blit(badguy3, (ex, ey))
    elif points >= 10:
        screen.blit(badguy2, (ex, ey))
    else:
        screen.blit(badguy, (ex, ey))


def bullet(bx, by):
    screen.blit(beam, (bx, by))

def bullet2(bx2, by2):
    screen.blit(beam, (bx2, by2))



def plane(x, y):
    screen.blit(ship, (x, y))

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()
        screen.blit(back, (0, 0))
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objs("A Bit Spacey", largeText, blue)
        TextRect.center = ((800/2),(600/2))
        screen.blit(TextSurf, TextRect)

        button("Play!",150,450,100,50,green,bright_green,game)
        button("Quit?",550,450,100,50,red,bright_red,quit)


        pygame.display.update()
        clock.tick(15)

def game():
    end = False
    x = 375
    y = 450
    x_change = 0
    y_change = 0
    by = y
    bx = x
    fire = False
    b_speed = 25
    count = 0
    cooldown = 30
    ex = 300
    ey = 15
    points = 0
    time = 1200
    seconds = 20
    shift = 4
    new = False
    newy = -1000
    newx = 400
    newc = 0
    b_count = 1
    count2 = 0
    shooted = False
    normal = False
    hard = False
    ultra = False
    imp = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_UP:
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    y_change = 10
                if event.key == pygame.K_SPACE:
                    fire = True




            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_SPACE:
                    None


        if x <= 0:
            x = 0
        if x >= display_width - 50:
            x = display_width - 50
        if y <= 0:
            y = 0
        if y >= display_height - 50:
            y = display_height - 50


        x += x_change
        y += y_change
        screen.blit(back, (0, 0))
        plane(x, y)
        enemy(ex, ey, points)
        if new == True:
            enemy(newx, newy, points)
        score(points)
        dif(points)
        #timer(seconds)




        if fire == True:
            by -= b_speed
            if count < 1:
                bx = x + 20
                count += 1
            bullet(bx, by)





        if by <= -40:
            count -= 1
            fire = False
            by = y
            bx = x + 20


        if by < ey+50 and by > ey and fire == True:
            if bx > ex and bx < ex+50 or bx+10 > ex and bx+10 < ex+50:
                points += 1
                ex = 100
                ey = 15

        if by < newy+50 and by > newy and fire == True:
            if bx > newx and bx < newx+50 or bx+10 > newx and bx+10 < newx+50:
                points += 1
                newx = 100
                newy = 15
                b_count = 1
        shift -= 1


        if shift <= 0:
            if count % 2 == 0:
                direct = random.randint(1, 3)
                direct2 = random.randint(1, 3)
            count2 += 1
            if direct == 1:
                ex += 15
            if direct == 2:
                ex -= 15
            if direct2 == 1:
                newx += 15
            if direct2 == 2:
                newx -= 15
            shift = 4

            if ey >= 75 and b_count == 1:
                new = True
                b_count = 2

            if new == True and newc == 0:
                newx = 400
                newy = 15
                enemy(newx, newy, points)
                newc = 1
            if points >= 10:
                noraml = True
            if points >= 20:
                hard = True
            if points >= 30:
                ultra = True
            if points >= 40:
                imp = True


            if count2 >= 20 or normal == True and count2 >= 16 or hard == True and count2 >= 12 or ultra == True and count2 >= 8 or imp == True and count2 >= 4:
                count2 = 0
                newx = 400
                newy += 60
                ex = 300
                ey += 60







        cooldown -= 1
        time -= 1

        if time <= 0:
            None
            #crash(points)

        if time % 60 == 0:
            seconds = int(time/60)

        if ey >= 600 or newy >= 600:
            crash(points)


        pygame.display.update()
        clock.tick(60)

game_intro()
game()
quit()
