import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_main_menu(game) -> None:
    """
    Draws main menu
    """
    title_font = pygame.font.Font(None, min(game.screen.get_width() // 10, game.screen.get_height() // 10))
    title_str = title_font.render("Space Invaders", True, BLACK)
    title_x, title_y = (game.screen.get_width() - title_str.get_width()) // 2, game.screen.get_height() * 0.25

    button_font = pygame.font.Font(None, min(game.screen.get_width() // 15, game.screen.get_height() // 15))

    play_str = button_font.render("Play", True, BLACK)
    play_x, play_y = (game.screen.get_width() - play_str.get_width()) // 2, game.screen.get_height() * 0.45

    # difficult_str = font.render("Change difficulty", True, BLACK)

    quit_str = button_font.render("Quit", True, BLACK)
    quit_x, quit_y = (game.screen.get_width() - quit_str.get_width()) // 2, play_y + quit_str.get_height() + 30

    # Draw background
    game.screen.blit(game.background,(0,0))

    # Draw title
    pygame.draw.rect(game.screen, WHITE, (title_x, title_y, title_str.get_width(), title_str.get_height()))
    game.screen.blit(title_str, (title_x, title_y))

    # Draw play option
    pygame.draw.rect(game.screen, WHITE, (play_x, play_y, play_str.get_width(), play_str.get_height()))
    game.screen.blit(play_str, (play_x, play_y))

    # TODO: Draw Difficulty selector

    # Draw quit option
    pygame.draw.rect(game.screen, WHITE, (quit_x, quit_y, quit_str.get_width(), quit_str.get_height()))
    game.screen.blit(quit_str, (quit_x, quit_y))


def draw_pause_menu(game) -> None:
    """
    Draws pause screen
    """
    game.screen.blit(game.background, (0, 0))
    pygame.draw.rect(game.screen, "white", [380, 150, 510, 50], 0, 10)
    game.screen.blit(
        game.font.render("Game Paused: Press Escape to Resume", True, "black"),
        (400, 160),
    )
