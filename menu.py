import pygame  # type: ignore
from typing import List

from state import State
from button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Menu:
    def __init__(self, background, buttons) -> None:
        self.background = background
        self.buttons: List[Button] = []

def draw_main_menu(game) -> None:
    """
    Draws main menu
    """

    title = Button(
            "Space Invaders",
            None,
            75,
            game.screen.get_width() // 2,
            game.screen.get_height() * 0.35,
            WHITE,
            (136, 8,8),
            BLACK
            )

    play_button = Button(
            "Play",
            None,
            50,
            game.screen.get_width() // 2,
            game.screen.get_height() * 0.55,
            WHITE,
            (136, 8,8),
            BLACK
            )

    quit_button = Button(
            "Quit",
            None,
            50,
            game.screen.get_width() // 2,
            game.screen.get_height() * 0.65,
            WHITE,
            (136, 8,8),
            BLACK
            )

    title.draw(game.screen)
    play_button.draw(game.screen)
    quit_button.draw(game.screen)
    print(title.hovered)


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


# Make real menu class
def handle_main_menu(game) -> None:
    pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = State.EXIT
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button


def handle_pause_menu(game) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = State.EXIT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game.state = State.RUNNING
