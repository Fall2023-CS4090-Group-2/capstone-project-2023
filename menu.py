import pygame  # type: ignore
from typing import List

from state import State
from difficulty import Difficulty
from button import Button
from ui import HIGHLIGHT_COLOR, BACKGROUND_COLOR, TEXT_COLOR


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

    def update_score(self, game):
        self.game = game


def create_main_menu(game) -> Menu:
    """
    Create Menu object for the main menu
    """
    title_button = Button(
        "Mining Answers with Joe",
        game,
        None,
        75,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.25,
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
        game.screen.get_height() * 0.45,
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
        game.screen.get_height() * 0.55,
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
        game.screen.get_height() * 0.55,
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
        game.screen.get_height() * 0.55,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    music_button = Button(
        "Toggle Music",
        game,
        State.MAIN_MUSIC,
        50,
        game.screen.get_width() // 2,
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
            music_button,
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
        game.screen.get_height() * 0.85,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    music_button = Button(
        "Toggle Music",
        game,
        State.PAUSE_MUSIC,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.75,
        BACKGROUND_COLOR,
        HIGHLIGHT_COLOR,
        TEXT_COLOR,
    )

    return Menu(
        game, [pause_button, resume_button, main_menu_button, quit_button, music_button]
    )


def create_game_over_menu(game) -> Menu:
    """
    Create Menu object for the losing menu
    """
    result_button = Button(
        "Oh no! You've been crushed to death!",
        game,
        State.GAME_OVER,
        75,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.45,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )

    correct_button = Button(
        f"Questions Correct: {game.num_correct}",
        game,
        State.GAME_OVER,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.52,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )
    
    incorrect_button = Button(
        f"Questions Incorrect: {game.num_incorrect}",
        game,
        State.GAME_OVER,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.57,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
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

    return Menu(game, [result_button, correct_button, incorrect_button, main_menu_button, quit_button])


def update_game_over_menu(game) -> None:
    """
    Create Menu object for the winning menu
    """

    result_button = Button(
        f"You've scored {game.score} points!",
        game,
        State.GAME_OVER,
        75,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.45,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )

    correct_button = Button(
        f"Questions Correct: {game.num_correct}",
        game,
        State.GAME_OVER,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.52,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )

    incorrect_button = Button(
        f"Questions Incorrect: {game.num_incorrect}",
        game,
        State.GAME_OVER,
        50,
        game.screen.get_width() // 2,
        game.screen.get_height() * 0.57,
        BACKGROUND_COLOR,
        BACKGROUND_COLOR,
        TEXT_COLOR,
    )

    game.game_over_menu.buttons[0] = result_button
    game.game_over_menu.buttons[1] = correct_button
    game.game_over_menu.buttons[2] = incorrect_button
