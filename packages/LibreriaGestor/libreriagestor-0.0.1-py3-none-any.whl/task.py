class Task:
    def __init__(self, description, responsible, start_date, deadline, importance, difficulty, completed=False):
        self.description = description
        self.responsible = responsible
        self.start_date = start_date
        self.deadline = deadline
        self.importance = importance
        self.difficulty = difficulty
        self.completed = completed
