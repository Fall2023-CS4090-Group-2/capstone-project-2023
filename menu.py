import pygame  # type: ignore
from typing import List

from state import State
from difficulty import Difficulty
from button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (18, 71, 52)
GOLD = (209, 184, 136)
HIGHLIGHT_GOLD = (219, 194, 146)

PETRA = (172, 161, 153) # this color is darker then pebble
PEBBLE = (214, 209, 202)

TEXT_COLOR = BLACK
HIGHLIGHT_COLOR = GREEN
BACKGROUND_COLOR = GOLD

class Menu:
    def __init__(self, game, buttons) -> None:
        self.game = game
        self.buttons: List[Button] = buttons

    def draw(self) -> None:
        """
        Draws menu
        """
        self.game.screen.blit(self.game.background, (0, 0))
        for button in self.buttons:
            button.is_hovered()
            button.draw(self.game.screen)

    def handle_menu(self) -> None:
        """
        Handles inputs for menu
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.state = State.EXIT
            # Left mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    if (
                        button.hovered
                        and button.state != None
                        and button.state in State
                    ):
                        self.game.state = button.state
                    elif (
                        button.hovered
                        and button.state != None
                        and button.state in Difficulty
                    ):
                        self.game.difficulty = button.state

            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
                and self.game.state in [State.RUNNING, State.PAUSED]
            ):
                self.game.state = State.RUNNING


def create_main_menu(game) -> Menu:
    """
    Create Menu object for the main menu
    """
    title_button = Button(
        "Miner Quiz",
        game,
        None,
        75,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.35,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )

    play_button = Button(
        "Play",
        game,
        State.RUNNING,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.55,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    easy_button = Button(
        "Easy",
        game,
        Difficulty.EASY,
        50,
        game.screen.get_width() // 2 - 150,
        game.screen.get_height() * 0.65,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    medium_button = Button(
        "Medium",
        game,
        Difficulty.MEDIUM,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.65,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    hard_button = Button(
        "Hard",
        game,
        Difficulty.HARD,
        50,
        game.screen.get_width() // 2 + 150,
        game.screen.get_height() * 0.65,
        
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,

    )

    quit_button = Button(
        "Quit",
        game,
        State.EXIT,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.75,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    return Menu(
        game,
        [
            title_button,
            play_button,
            easy_button,
            medium_button,
            hard_button,
            quit_button,
        ],
    )


def create_pause_menu(game) -> Menu:
    """
    Create Menu object for the pause menu
    """
    pause_button = Button(
        "PAUSED: Press escape to resume",
        game,
        None,
        75,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.45,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )

    resume_button = Button(
        "Resume game",
        game,
        State.RUNNING,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.55,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    main_menu_button = Button(
        "Back to main menu",
        game,
        State.MAIN_MENU,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.65,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    quit_button = Button(
        "Quit game",
        game,
        State.EXIT,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.75,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    return Menu(game, [pause_button, resume_button, main_menu_button, quit_button])
