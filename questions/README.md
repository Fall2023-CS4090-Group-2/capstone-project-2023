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

Just delete questions from the `json` file or completely remove the file if you don't like any of the questions.
