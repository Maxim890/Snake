import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 800 # Зададим размер игрового поля через две переменные.
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))  # Задаём размер игрового поля
pygame.display.set_caption('Змейка')  # Добавляем название игры.
clock = pygame.time.Clock()
snake_block = 10  # Укажем в переменной стандартную величину сдвига положения змейки при нажатии на клавиши.
snake_speed = 15  # Ограничим скорость движения змейки.
font_style = pygame.font.SysFont("bahnschrift", 25)  # Укажем название шрифта и его размер для системных сообщений,
# например, при завершении игры.
score_font = pygame.font.SysFont("comicsansms", 35)  # Укажем шрифт и его размер для отображения счёта. Это мы реализуем
# очень скоро.


def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):  # Создадим функцию, которая будет показывать нам сообщения на игровом экране.
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():  # Описываем всю игровую логику в одной функции.
    game_over = False  # Создаём переменную, которая поможет нам контролировать статус игры — завершена она или нет.
    # Изначально присваиваем значение False, то есть игра продолжается.
    game_close = False
    x1 = dis_width / 2  # Стартовое положение змейки по осям рассчитывается
    y1 = dis_height / 2
    x1_change = 0  # Создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки
    # по оси х.
    y1_change = 0  # создаём переменную, которой в цикле while будут присваиваться значения изменения положения змейки
    # по оси y.
    snake_List = []  # Создаём список, в котором будем хранить показатель текущей длины змейки.
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # Создаём переменную, которая будет
    # указывать расположение еды по оси х.
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # Создаём переменную, которая будет
    # указывать расположение еды по оси y.
    while not game_over:
        while game_close == True:  # Явно укажем, что если координаты змейки выходят за рамки игрового поля, то игра
            # должна закончиться.
            dis.fill(blue)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)  # Сообщение, которое появляется
            # при проигрыше. В нашем случае — при выходе змейки за пределы игрового поля.
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Добавляем считывание направления движений с клавиатуры.
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change  # Записываем новое значение положения змейки по оси х.
        y1 += y1_change  # Записываем новое значение положения змейки по оси y.
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []  # Создаём список, в котором будет храниться показатель длины змейки при движениях.
        snake_Head.append(x1)  # Добавляем значения в список при изменении по оси х.
        snake_Head.append(y1)  # Добавляем значения в список при изменении по оси y.
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]  # Удаляем первый элемент в списке длины змейки, чтобы она не увеличивалась сама по себе
            # при движениях.
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:  # Указываем, что в случаях, если координаты головы змейки совпадают с
    # координатами еды, еда появляется в новом месте, а длина змейки увеличивается на одну клетку.
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop()