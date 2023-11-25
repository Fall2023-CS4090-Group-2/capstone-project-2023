import pygame  # type: ignore
from typing import List

from state import State
from button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Menu:
    def __init__(self, screen, background, buttons) -> None:
        self.background = background
        self.buttons: List[Button] = buttons
        self.screen = screen

    def draw(self) -> None:
        """
        Draws menu
        """
        self.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.is_hovered()
            button.draw(self.screen)

    def handle_menu(self, game) -> None:
        """
        Handles inputs for menu
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.state = State.EXIT
            # Left mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in game.main_menu.buttons:
                    if button.hovered and button.state != None:
                        game.state = button.state


def create_main_menu(screen, background) -> Menu:
    title_button = Button(
            "Space Invaders",
            None,
            75,
            screen.get_width() // 2,
            screen.get_height() * 0.35,
            WHITE,
            WHITE,
            BLACK
            )

    play_button = Button(
            "Play",
            State.RUNNING,
            50,
            screen.get_width() // 2,
            screen.get_height() * 0.55,
            WHITE,
            (136, 8,8),
            BLACK
            )

    quit_button = Button(
            "Quit",
            State.EXIT,
            50,
            screen.get_width() // 2,
            screen.get_height() * 0.65,
            WHITE,
            (136, 8,8),
            BLACK
            )

    return Menu(screen, background, [title_button, play_button, quit_button])



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


# TODO: Remove and add to handle_menu
def handle_pause_menu(game) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = State.EXIT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game.state = State.RUNNING
