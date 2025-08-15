import sys

class CleanCodePractice:
    def __init__(self):
        self.exercises = self.load_exercises()

    def load_exercises(self):
        return [
            {'id': 1, 'title': 'Naming Conventions', 'description': 'Refactor variable names to be more descriptive.'},
            {'id': 2, 'title': 'Function Size', 'description': 'Split large functions into smaller, more manageable ones.'},
            {'id': 3, 'title': 'Code Readability', 'description': 'Improve the readability of the given code snippet.'}
        ]

    def display_exercises(self):
        print("Available Exercises:")
        for exercise in self.exercises:
            print(f"{exercise['id']}. {exercise['title']} - {exercise['description']}")

    def run(self):
        self.display_exercises()
        choice = input("Select an exercise by number: ")
        self.start_exercise(choice)

    def start_exercise(self, exercise_id):
        try:
            exercise_id = int(exercise_id)
            exercise = self.exercises[exercise_id - 1]
            print(f"Starting exercise: {exercise['title']}\n\n{exercise['description']}")
            # Here would go the logic for the interactive exercise
        except (ValueError, IndexError):
            print("Invalid selection. Please choose a valid exercise number.")

if __name__ == '__main__':
    tool = CleanCodePractice()
    tool.run()