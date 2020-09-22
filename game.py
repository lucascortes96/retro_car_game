import pygame
import random
from car import Car


pygame.init()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
carcrash = 0
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

SCREENWIDTH = 700
SCREENHEIGHT = 500
# Open a window 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car Racing')

font = pygame.font.Font(None, 100)
text = font.render("Space bar to pause you crash you die", 100, (100,100,100))
screen.blit(text,(100,100))






## Program Loop
def main(): 
    all_sprites_list = pygame.sprite.Group()
    playerCar = Car(RED, 40, 60, 50)
    playerCar.rect.x = 160
    playerCar.rect.y = SCREENHEIGHT - 100
    
    car1 = Car(PURPLE, 60, 80, random.randint(50,100))
    car1.rect.x = 358
    car1.rect.y = -100
    
    car2 = Car(YELLOW, 60, 80, random.randint(50,100))
    car2.rect.x = 252
    car2.rect.y = -400
    
    car3 = Car(CYAN, 60, 80, random.randint(50,100))
    car3.rect.x = 160
    car3.rect.y = -300
    
    car4 = Car(BLUE, 60, 80, random.randint(50,100))
    car4.rect.x = 460
    car4.rect.y = -400
    
    all_sprites_list.add(playerCar)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    
    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)
    ##Carry on until user exit 
    carryOn = True 
# Control screen update 
    clock = pygame.time.Clock()
    speed = 1
    carryOn = True
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if playerCar.rect.x < 140:
                play_again()
            if playerCar.rect.x > 570:
                play_again()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    playerCar.moveRight(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            speed += 0.05
        if keys[pygame.K_DOWN]:
            speed -= 0.05
        if keys[pygame.K_r]:
            play_again()
            
        
        
        for car in all_coming_cars:
            car.moveForward(speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50,100))
                car.repaint(random.choice(colorList))
                car.rect.y = -200
            car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
        for car in car_collision_list:
            print('Crash')
            play_again()
        if carryOn == False:
            gameover = font.render("Press R to restart", False, (255,255,255))
            rect = gameover.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(gameover, rect)
        
        all_sprites_list.update()
        screen.fill(WHITE)
        # Draw shapes and lines 
        pygame.draw.rect(screen, GREEN, [0, 0, 137.5, 500],0)
        pygame.draw.rect(screen, GREY, [142.5,0, 100, 500], 0)
        pygame.draw.rect(screen, GREY, [247.5, 0, 100, 500], 0)
        pygame.draw.rect(screen, GREY, [352.5, 0, 100, 500], 0)
        pygame.draw.rect(screen, GREY, [457.5, 0, 100, 500], 0)
        pygame.draw.rect(screen, GREEN, [562.5, 0, 150, 500], 0)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
        

bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)
    
def play_again():
    text = bigfont.render('Play again?', 13, (0, 0, 0))
    textx = SCREENWIDTH / 2 - text.get_width() / 2
    texty = SCREENHEIGHT / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                               (textx_size + 10, texty_size +
                                                10)))

    screen.blit(text, (SCREENWIDTH / 2 - text.get_width() / 2,
                       SCREENHEIGHT / 2 - text.get_height() / 2))

    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= textx - 5 and x <= textx + textx_size + 5:
                    if y >= texty - 5 and y <= texty + texty_size + 5:
                        in_main_menu = False
                        main()
   
    
main()
play_again()
pygame.quit()
