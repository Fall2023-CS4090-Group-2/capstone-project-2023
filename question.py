from typing import List


class Question:
    def __init__(self, question: str, options: List[str], answer: str):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, answer: str):
        return answer == self.answer
