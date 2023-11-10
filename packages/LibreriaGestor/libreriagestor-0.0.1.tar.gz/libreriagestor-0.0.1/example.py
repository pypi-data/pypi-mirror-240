#%%
from project import Project
from visualization import plot_task_status

# Crear un proyecto o cargar un proyecto existente
project1 = Project("Proyecto 1")
project2 = Project("Proyecto 2")

# Agregar tareas al proyecto 1
project1.add_task("Tarea 1 Proyecto 1", "Juan", "2023-11-01", "2023-11-15", 3, 2)
project1.add_task("Tarea 2 Proyecto 1", "Maria", "2023-11-05", "2023-11-20", 2, 1)

# Agregar tareas al proyecto 2
project2.add_task("Tarea 1 Proyecto 2", "Carlos", "2023-11-10", "2023-11-25", 1, 3)
project2.add_task("Tarea 2 Proyecto 2", "Laura", "2023-11-15", "2023-12-01", 2, 2)

# Visualizar el estado de las tareas antes de la actualización
print("Estado de las tareas antes de la actualización:")
print("Proyecto 1:")
plot_task_status(project1)
print("Proyecto 2:")
plot_task_status(project2)

# Actualizar tareas en el proyecto 1
project1.update_task("Tarea 1 Proyecto 1", completed=True)
project1.update_task("Tarea 2 Proyecto 1", importance=1)

# Actualizar tareas en el proyecto 2
project2.update_task("Tarea 1 Proyecto 2", completed=True)
project2.update_task("Tarea 2 Proyecto 2", responsible="Roberto")

# Visualizar el estado de las tareas después de la actualización
print("\nEstado de las tareas después de la actualización:")
print("Proyecto 1:")
plot_task_status(project1)
print("Proyecto 2:")
plot_task_status(project2)

# %%
project2.add_task("Tarea 3 Proyecto 2", "Pedro", "2023-11-19", "2023-12-21", 2, 2)

# %%
print("Proyecto 2:")
plot_task_status(project2)
# %%
project2.update_task("Tarea 3 Proyecto 2", completed=True)
plot_task_status(project2)


# %%
print("Estado actual de las tareas en el proyecto:")
print("Proyecto 1:")
print(project1.get_tasks())
print("Proyecto 2:")
print(project2.get_tasks())
# %%
