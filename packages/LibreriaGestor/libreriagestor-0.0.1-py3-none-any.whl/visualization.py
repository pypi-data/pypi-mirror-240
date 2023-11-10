import matplotlib.pyplot as plt

def plot_task_status(project):
    completed_tasks = sum(1 for task in project.tasks['completed'] if task)
    pending_tasks = len(project.tasks) - completed_tasks

    labels = ['Completadas', 'Pendientes']
    sizes = [completed_tasks, pending_tasks]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Estado de las Tareas')
    plt.show()
