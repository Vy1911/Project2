import pygame
from config import BLACK, WHITE, screen, RED

from sprites import Button



def read_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0


def write_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


def start_screen(high_score):
    from game import game_loop
    try:
        background_image = pygame.image.load("background1.jpg").convert_alpha()
        background_image = pygame.transform.scale(background_image, (390, 620))  # Resize to screen size
    except pygame.error as e:
        print(f"Error loading background image: {e}")
        return


    font = pygame.font.SysFont("Arial", 24)


    play_button = Button(175, 320, font.render("Play", True, WHITE))
    instructions_button = Button(145, 420, font.render("Instructions", True, WHITE))
    exit_button = Button(175, 520, font.render("Exit", True, WHITE))

    while True:

        screen.blit(background_image, (0, 0))


        play_button.draw()
        instructions_button.draw()
        exit_button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked():
                    game_loop()
                    return
                elif instructions_button.is_clicked():
                    instructions_screen()
                    return
                elif exit_button.is_clicked():
                    pygame.quit()
                    return

def instructions_screen():
    from game import game_loop
    back_button = Button(50, 500, pygame.font.SysFont("Arial", 24).render("Back", True, WHITE))
    play_button = Button(250, 500, pygame.font.SysFont("Arial", 24).render("Play", True, WHITE))

    while True:
        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 24)
        instructions_text = [
            "Use arrow keys to move left and right.",
            "Press SPACE to shoot bullets.",
            "Avoid enemies and score points by shooting them!",
            "Do not let enemies hit the bottom",
            "Reaching 100 points to get win!!",
        ]


        y = 150
        for line in instructions_text:
            text = font.render(line, True, WHITE)
            screen.blit(text, (20, y))
            y += 40


        back_button.draw()
        play_button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked():
                    start_screen(read_high_score())
                    return
                elif play_button.is_clicked():
                    game_loop()
                    return


def game_over_screen(score, high_score):
    font = pygame.font.SysFont("Arial", 24)
    text1 = font.render("Game Over!", True, RED)
    text2 = font.render("Press R to Restart or E to Exit", True, WHITE)
    score_text = font.render(f"Your Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text1, (140, 200))
    screen.blit(text2, (80, 250))
    screen.blit(score_text, (130, 300))
    screen.blit(high_score_text, (130, 350))
    pygame.display.flip()


def win_screen():
    from game import game_loop
    font = pygame.font.SysFont("Arial", 36)
    text = font.render("You Win!", True, (0, 255, 0))
    instruction_text = font.render("Press R to Restart or E to Exit", True, (255, 255, 255))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text, (120, 250))
        screen.blit(instruction_text, (50, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()
                    return
                elif event.key == pygame.K_e:
                    pygame.quit()
                    return


def quit_confirmation_screen():
    yes_button = Button(100, 300, pygame.font.SysFont("Arial", 24).render("Yes", True, WHITE))
    no_button = Button(220, 300, pygame.font.SysFont("Arial", 24).render("No", True, WHITE))

    while True:
        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Do you want to quit the game?", True, RED)

        screen.blit(text, (50, 200))

        yes_button.draw()
        no_button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.is_clicked():
                    pygame.quit()
                    return True
                elif no_button.is_clicked():
                    return False