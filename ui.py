import pygame  # type: ignore

PADDING = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (18, 71, 52)
GOLD = (209, 184, 136)
HIGHLIGHT_GOLD = (219, 194, 146)

PETRA = (172, 161, 153)  # this color is darker then pebble
PEBBLE = (214, 209, 202)

TEXT_COLOR = BLACK
HIGHLIGHT_COLOR = GREEN
BACKGROUND_COLOR = GOLD


def render_text(font, text, max_width):
    """
    Render text and truncate if it exceeds max_width
    """
    rendered_text = font.render(text, True, TEXT_COLOR)
    if rendered_text.get_width() > max_width:
        ellipsis = font.render("...", True, TEXT_COLOR)
        remaining_width = max_width - ellipsis.get_width()
        truncated_text = ""
        for char in text[::-1]:
            if remaining_width >= 0:
                truncated_text = char + truncated_text
                remaining_width -= font.size(char)[0]
            else:
                break
        return font.render(truncated_text, True, TEXT_COLOR)
    return rendered_text


def draw_answer(game) -> None:
    """
    Draws your current typed out answer
    """
    # Don't draw if multiple choice
    if len(game.selected_question.options) > 0:
        return

    if game.player.answer_mode:
        background_color = HIGHLIGHT_COLOR
    else:
        background_color = BACKGROUND_COLOR

    # Calculate the height of the background rectangle
    total_height = game.font.get_height() + 2 * PADDING

    # Draw the colored background rectangle
    pygame.draw.rect(
        game.screen,
        background_color,
        pygame.Rect(
            game.screen.get_width() / 4 - PADDING,
            game.screen.get_height() - game.font.get_height() - 2 * PADDING,
            game.screen.get_width() / 2 + 2 * PADDING,
            total_height,
        ),
    )

    answer_str = game.font.render("Answer: ", True, TEXT_COLOR)
    text_rect = answer_str.get_rect(
        topleft=(
            game.screen.get_width() / 4,
            game.screen.get_height() - total_height + PADDING,
        )
    )
    game.screen.blit(answer_str, text_rect.topleft)

    max_text_width = game.screen.get_width() / 2
    answer_text_rendered = render_text(
        game.font,
        game.answer,
        max_text_width - answer_str.get_width() - PADDING,
    )
    text_rect = answer_text_rendered.get_rect(
        topleft=(
            game.screen.get_width() / 4 + answer_str.get_width(),
            game.screen.get_height() - total_height + PADDING,
        )
    )
    game.screen.blit(answer_text_rendered, text_rect.topleft)


def draw_bullets(game) -> None:
    """
    Draws bullet value
    """
    bullet_str = game.font.render(
        f"Bullet: {str(game.num_bullets)}", True, (255, 255, 255)
    )
    game.screen.blit(
        bullet_str,
        (
            game.screen.get_width() / 5 + PADDING,
            game.font.get_height() - PADDING,
        ),
    )


def draw_health(game) -> None:
    """
    Draws health value
    """
    health_str = game.font.render(f"Health: {str(game.health)}", True, (255, 255, 255))
    game.screen.blit(
        health_str,
        (
            PADDING,
            game.font.get_height() - PADDING,
        ),
    )


def draw_score(game) -> None:
    """
    Draws score value
    """
    score_str = game.font.render(f"Score: {str(game.score)}", True, (255, 255, 255))
    game.screen.blit(
        score_str,
        (
            game.screen.get_width() / 10 + PADDING,
            game.font.get_height() - PADDING,
        ),
    )


def draw_questions(game) -> None:
    """
    Draws current question
    """
    start_y = PADDING
    options_vertical_spacing = 5
    question_str = game.font.render(
        f"Question: {game.selected_question.question}", True, TEXT_COLOR
    )
    max_width = question_str.get_width()

    # Calculate maximum width if options are present
    if len(game.selected_question.options) > 0:
        max_width = max(
            max_width,
            *[
                game.font.render(option, True, TEXT_COLOR).get_width()
                for option in game.selected_question.options
            ],
        )

    # Calculate the height needed for the rectangle background
    total_height = (len(game.selected_question.options) + 1) * (
        game.font.get_height() + options_vertical_spacing
    )

    # Draw brown rectangle background
    pygame.draw.rect(
        game.screen,
        BACKGROUND_COLOR,
        (
            game.screen.get_width() * 0.75 - max_width - PADDING,
            start_y,
            max_width + 2 * PADDING,
            total_height,
        ),
    )

    # Draw question
    game.screen.blit(
        question_str, (game.screen.get_width() * 0.75 - max_width - PADDING, start_y)
    )

    # Draw options
    for idx, option in enumerate(game.selected_question.options):
        start_y += game.font.get_height() + options_vertical_spacing
        option_str = game.font.render(f"{idx+1}. {option}", True, TEXT_COLOR)
        game.screen.blit(
            option_str, (game.screen.get_width() * 0.75 - max_width - PADDING, start_y)
        )
