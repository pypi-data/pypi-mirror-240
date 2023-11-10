from excel_manager import ExcelManager
from task import Task
import pandas as pd

class Project(ExcelManager):
    def __init__(self, name, filename="tasks.xlsx"):
        super().__init__(filename)
        self.name = name
        self.tasks = self.load_data()

    def add_task(self, description, responsible, start_date, deadline, importance, difficulty, completed=0):
        task_data = pd.DataFrame([[description, responsible, start_date, deadline, importance, difficulty, completed]],
                                 columns=["description", "responsible", "start_date", "deadline", "importance", "difficulty", "completed"])
        self.update_data(task_data)
        return Task(description, responsible, start_date, deadline, importance, difficulty, completed)

    def update_task(self, tarea, is_completed=None, **kwargs):
        task_index = self.tasks[self.tasks['description'] == tarea].index
        if len(task_index) > 0:
            task_index = task_index[0]
            if is_completed is not None:
                self.tasks.at[task_index, 'completed'] = bool(is_completed)
            for key, value in kwargs.items():
                self.tasks.at[task_index, key] = value
            self.save_data(self.tasks)
        else:
            print(f"Tarea '{tarea}' no encontrada.")

    
    def get_tasks(self):
        return [Task(**task) for _, task in self.tasks.iterrows()]
