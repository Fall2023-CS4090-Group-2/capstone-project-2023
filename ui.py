PADDING = 10

WHITE = (255, 255, 255)
LIGHT_YELLOW = (227, 207, 87)


def draw_answer(game) -> None:
    """
    Draws your current typed out answer
    """
    if game.player.answer_mode:
        color = LIGHT_YELLOW
    else:
        color = WHITE
    answer_str = game.font.render("Answer: ", True, color)
    game.screen.blit(
        answer_str,
        (
            game.screen.get_width() / 4,
            game.screen.get_height() - game.font.get_height() - PADDING,
        ),
    )
    game.screen.blit(
        game.font.render(game.answer, True, WHITE),
        (
            game.screen.get_width() / 4 + answer_str.get_width(),
            game.screen.get_height() - game.font.get_height() - PADDING,
        ),
    )


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
            bullet_str.get_width() * 3
            + PADDING,  # Kind of scuffed position but its there
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
            score_str.get_width() * 1.75 + PADDING,
            game.font.get_height() - PADDING,
        ),
    )


def draw_questions(game) -> None:
    """
    Draws current questions
    """
    # TODO: Probably make this wrap too
    max_width = 0
    start_y = game.screen.get_height() * 0.04
    vertical_spacing = 20
    options_vertical_spacing = 5
    num_questions = 3

    # Calculate maximum width
    for question in game.questions[:num_questions]:
        max_width = max(
            max_width,
            game.font.render(f"Question #: {question.question}", True, WHITE).get_width(),
            *[game.font.render(option, True, WHITE).get_width() for option in question.options]
        )

    # Draw questions and options with right alignment
    for idx, question in enumerate(game.questions[:num_questions]):
        if question is game.selected_question:
            color = LIGHT_YELLOW
        else:
            color = WHITE

        # Draw question
        question_str = game.font.render(f"Question {idx+1}: {question.question}", True, color)
        game.screen.blit(question_str, (game.screen.get_width() - max_width - PADDING, start_y))

        # Draw options
        for option in question.options:
            start_y += game.font.get_height() + options_vertical_spacing
            option_str = game.font.render(option, True, color)
            game.screen.blit(option_str, (game.screen.get_width() - max_width - PADDING, start_y))

        # Adjust y for the next set of question and options
        start_y += game.font.get_height() + vertical_spacing
