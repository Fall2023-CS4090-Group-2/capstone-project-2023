import pygame  # type: ignore

from difficulty import Difficulty
from ui import PADDING


class Button:
    def __init__(
        self,
        text,
        game,
        state,
        font_size,
        x,
        y,
        color,
        hover_color,
        text_color,
        padding=PADDING,
    ) -> None:
        # Text
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_str = self.font.render(self.text, True, text_color)

        self.game = game
        self.state = state

        # Position
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.padding = padding
        self.rect.width, self.rect.height = self.text_str.get_size()
        self.rect.width += self.padding
        self.rect.height += self.padding
        self.rect.center = (x, y)

        # Color
        self.hovered = False
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen) -> None:
        if self.hovered or self.is_selected_difficulty():
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=5)
        else:
            if self.color != None:
                pygame.draw.rect(screen, self.color, self.rect, border_radius=5)

        text_rect = self.text_str.get_rect(center=self.rect.center)
        screen.blit(self.text_str, text_rect.topleft)

    def is_hovered(self) -> None:
        if self.state != None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.hovered = self.rect.collidepoint(mouse_x, mouse_y)

    def is_selected_difficulty(self) -> bool:
        if self.state != None:
            return self.state in Difficulty and self.game.difficulty == self.state
        else:
            return False
