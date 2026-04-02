import pygame
import random

pygame.init()
pygame.font.init()
pygame.font.get_fonts ()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True
SQSIZE = 20
FPS = 10
snake = [(300, 200), (280, 200), (260, 200)]
SNAKE_COLOR = (57, 255, 20)
x = 600/2
y = 400/2
vitesse_x = SQSIZE
vitesse_y = 0
apple_x = random.randrange(20, 580, SQSIZE)
apple_y = random.randrange(40, 380, SQSIZE)
font=pygame.font.SysFont(None, 55)
font_score = pygame.font.SysFont(None, 25)
gameover = font.render("GAME OVER",1,(255,255,255))
score = 0
go = False
apple = pygame.image.load("apple.png")
apple.convert()
apple = pygame.transform.scale(apple, (SQSIZE, SQSIZE))

while running:
    move = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and move == False:
            if event.key == pygame.K_UP and vitesse_y == 0:
                vitesse_x = 0
                vitesse_y = -SQSIZE
                move = True
            elif event.key == pygame.K_DOWN and vitesse_y == 0:
                vitesse_x = 0
                vitesse_y = SQSIZE
                move = True
            elif event.key == pygame.K_LEFT and vitesse_x == 0:
                vitesse_x = -SQSIZE
                vitesse_y = 0
                move = True
            elif event.key == pygame.K_RIGHT and vitesse_x == 0:
                vitesse_x = SQSIZE
                vitesse_y = 0
                move = True

    if not go:
        head_x = snake[0][0] + vitesse_x
        head_y = snake[0][1] + vitesse_y
        new_head = [head_x, head_y]
        if snake[0][0] == apple_x and snake[0][1] == apple_y:
            apple_x = random.randrange(20, 580, SQSIZE)
            apple_y = random.randrange(40, 380, SQSIZE)
            snake.append(snake[-1])
            score += 1
            if (score % 5 == 0):
                FPS += 1
        elif new_head in snake or head_x < 20 or head_x >= 580 or head_y < 20 or head_y >= 380:
            go = True
        else :
            snake.insert(0, new_head)
            snake.pop()
        pass

    screen.fill("black")

    if go:
        pygame.draw.rect(screen, (255,255,255), (0, 0, 600, 400), 20)
        screen.blit(apple, (apple_x, apple_y))
        score_text = font_score.render("Score: " + str(score), 1, (0, 0, 0))
        screen.blit(score_text, (5, 5))
        for segment in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], SQSIZE, SQSIZE))
        screen.blit(gameover, (200, 150))
        pygame.display.flip()
        pass

    else:
        pygame.draw.rect(screen, (255,255,255), (0, 0, 600, 400), 20)
        screen.blit(apple, (apple_x, apple_y))
        score_text = font_score.render("Score: " + str(score), 1, (0, 0, 0))
        screen.blit(score_text, (5, 5))
        for segment in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], SQSIZE, SQSIZE))
        pygame.display.flip()
        pass

    clock.tick(FPS)
pygame.quit()

