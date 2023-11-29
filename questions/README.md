## Adding questions to game

To add new questions to the game add a `.json` file to this directory with the shape:

``` json
[
  {
    "question": "What is the capital of France?",
    "options": ["Berlin", "Paris", "Madrid", "Rome"],
    "answer": "Paris"
  },
  {
    "question": "Which planet is known as the Red Planet?",
    "options": ["Earth", "Mars", "Jupiter", "Venus"],
    "answer": "Mars"
  },
  {
    "question": "What is 2 + 2?",
    "options": [],
    "answer": "4"
  },
  // More questions...
]
```

**NOTE:** `answer` should always be a string.


## Remove questions from the game

Delete questions from the `json` file or completely remove the `json` file if you don't like any of the questions.

**NOTE:** The game looks for all `.json` extensions. Any other extensions will be ignored.
