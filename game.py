import pygame
import time
from config import screen, home_icon, volume_on_icon, volume_off_icon, game_over_music,background, clock
from utils import read_high_score, quit_confirmation_screen, start_screen, win_screen, game_over_screen, write_high_score, screen, WHITE
from sprites import Player, Button, Bullet, Enemy


def game_loop():
    running = True
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # Initial enemy settings
    enemy_speed = 1
    spawn_rate = 3
    last_enemy_spawn_time = time.time()
    last_difficulty_increase_time = time.time()

    score = 0
    high_score = read_high_score()

    home_button = Button(10, 10, home_icon)
    volume_button = Button(390 - 50, 10, volume_on_icon)
    volume_on = True

    endgame_score_threshold = 50
    endgame = False
# music

    pygame.mixer.music.stop()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1, 0.0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Create a bullet
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

            if home_button.is_clicked():
                quit_game = quit_confirmation_screen()
                if quit_game:
                    pygame.quit()
                    return
                else:
                    start_screen(read_high_score())
                    return


            if volume_button.is_clicked():
                if volume_on:
                    pygame.mixer.music.pause()
                    volume_button.image = volume_off_icon
                    volume_on = False
                else:
                    pygame.mixer.music.unpause()
                    volume_button.image = volume_on_icon
                    volume_on = True

        if score >= 100:
            win_screen()
            return



        if score >= endgame_score_threshold:
            endgame = True

        if endgame:

            spawn_rate = 0.1
            enemy_speed = min(enemy_speed + 0.2, 15)
        else:
            if time.time() - last_difficulty_increase_time >= 10:
                spawn_rate = max(0.5, spawn_rate - 0.2)
                enemy_speed += 0.5
                last_difficulty_increase_time = time.time()

        if time.time() - last_enemy_spawn_time >= spawn_rate:
            enemy = Enemy(enemy_speed)
            all_sprites.add(enemy)
            enemies.add(enemy)
            last_enemy_spawn_time = time.time()

        all_sprites.update()

        for enemy in enemies:
            if enemy.rect.top > 620:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(game_over_music)
                pygame.mixer.music.play(-1, 0.0)
                game_over_screen(score, high_score)
                if score > high_score:
                    write_high_score(score)
                waiting = True
                while waiting:
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
                running = False
                break

        if pygame.sprite.spritecollide(player, enemies, True):
            pygame.mixer.music.stop()
            pygame.mixer.music.load(game_over_music)
            pygame.mixer.music.play(-1, 0.0)
            game_over_screen(score, high_score)
            if score > high_score:
                write_high_score(score)
            waiting = True
            while waiting:
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
            running = False


        for bullet in bullets:
            hits = pygame.sprite.spritecollide(bullet, enemies, True)
            if hits:
                bullet.kill()
                score += 1
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(390 // 2, 20))
        screen.blit(score_text, score_rect)

        home_button.draw()
        volume_button.draw()
        pygame.display.flip()
        clock.tick(60)


def main():
    high_score = read_high_score()
    start_screen(high_score)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    game_loop()
#run game
main()