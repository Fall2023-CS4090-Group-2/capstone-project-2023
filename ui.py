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
    height = 50
    # TODO: Align questions to right
    max_width = 0
    for idx, question in enumerate(game.questions[:4:1]):
        if question is game.selected_question:
            color = LIGHT_YELLOW
        else:
            color = WHITE
        question_str = game.font.render(
            f"Question {idx+1}: {question.question}", True, color
        )
        max_width = max(max_width, question_str.get_width())
        game.screen.blit(
            question_str, (game.screen.get_width() - max_width - PADDING, height)
        )
        for option in question.options:
            height += game.font.get_height()
            option_str = game.font.render(option, True, color)
            game.screen.blit(
                option_str, (game.screen.get_width() - max_width - PADDING, height)
            )
        height += game.font.get_height() * 2
