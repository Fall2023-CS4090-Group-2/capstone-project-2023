from typing import List
import json
import os
import random


class Question:
    def __init__(self, question: str, options: List[str], answer: str):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, answer: str):
        return answer == self.answer


def load_questions(directory_path="questions") -> List[Question]:
    """
    Loads each question json file in a directory into a List
    """
    questions = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)

            with open(file_path, "r") as file:
                try:
                    questions_dict = json.load(file)
                    for q in questions_dict:
                        questions.append(
                            Question(q["question"], q["options"], q["answer"])
                        )
                except json.JSONDecodeError as e:
                    print(f"Error loading {filename}: {e}")
        # randomly shuffle the questions
        random.shuffle(questions)
    return questions
