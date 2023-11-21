import pygame  # type: ignore


class Button:
    def __init__(
        self, text, action, font_size, x, y, color, hover_color, text_color
    ) -> None:
        # Text
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_str = self.font.render(self.text, True, text_color)

        self.action = action

        # Position
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.rect.width, self.rect.height = self.text_str.get_size()
        self.rect.center = (x, y)

        # Color
        self.hovered = False
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen) -> None:
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_rect = self.text_str.get_rect(center=self.rect.center)
        screen.blit(self.text_str, text_rect.topleft)

    def handle_click(self) -> None:
        if self.hovered:
            self.action()

    def is_hovered(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_x, mouse_y)
