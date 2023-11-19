import pygame


def draw_main_menu(screen, font, background) -> None:
    """
    Draws main menu
    """
    pass


def draw_pause_menu(screen, font, background) -> None:
    """
    Draws pause screen
    """
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, "white", [380, 150, 510, 50], 0, 10)
    screen.blit(
        font.render("Game Paused: Press Escape to Resume", True, "black"),
        (400, 160),
    )
