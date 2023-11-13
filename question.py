from typing import List


class Question:
    def __init__(self, question: str, options: List[str], answer: str):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, answer: str):
        return answer == self.answer


# TODO: Add more questions and find way to import questions. Maybe import questions in a JSON format?
def generate_questions() -> List[Question]:
    questions = []
    questions.append(Question("The answer is a A", ["A", "B", "C", "D"], "A"))
    questions.append(
        Question(
            "The answer is a Cat", ["Dog", "Cat", "Monkey", "Snailfish"], "Cat"
        )
    )
    questions.append(
        Question(
            "The answer is a Cat", ["Dog", "Cat", "Monkey", "Snailfish"], "Cat"
        )
    )
    return questions
