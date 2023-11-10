# Proyecto PyPi: Gestor de Proyectos

## Tabla de Contenidos

- [Introducción](#introducción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplos](#ejemplos)

## Introducción

El Gestor de Proyectos es una librería de Python diseñada para simplificar la gestión y organización de proyectos. Permite a los usuarios crear proyectos, asignar tareas, establecer fechas límite, asignar responsables y realizar un seguimiento del progreso del proyecto, todo desde la comodidad de su código Python.

## Características

- **Creación de Proyectos:** Crea nuevos proyectos especificando un nombre único.
- **Gestión de Tareas:** Agrega tareas con descripciones detalladas y con facilidades para ser editadas.
- **Actualización de Tareas:** Actualiza las tareas existentes para reflejar cambios en la responsabilidad, fechas límite y estado de finalización.
- **Visualizaciones Gráficas:** Genera visualizaciones gráficas para comprender fácilmente el estado del proyecto.

## Requisitos

- Python 3.x
- Pandas (instalable mediante `pip install pandas`)
- Matplotlib (instalable mediante `pip install matplotlib`)

## Instalación

Para instalar la librería, ejecuta el siguiente comando:

```bash
pip install proyecto-gestor
```

## Uso

Primero, importa la librería en tu script:

```python
from proyecto_gestor import Project, visualize
```

### Crear un Proyecto

Para crear un nuevo proyecto, utiliza el siguiente código:

```python
# Crear un nuevo proyecto
mi_proyecto = Project("Proyecto de Ejemplo")
```

### Agregar una Tarea al Proyecto

Puedes agregar tareas al proyecto de la siguiente manera:

```python
# Agregar una nueva tarea al proyecto
mi_tarea = mi_proyecto.add_task("Tarea 1", "Juan", "2023-11-01", "2023-11-15", 3, 2)
```

### Actualizar una Tarea Existente

Para actualizar una tarea existente, utiliza el método `update_task`:

```python
# Actualizar una tarea existente
mi_proyecto.update_task("Tarea 1", responsible="María", completed=True)
```

### Visualizar el Estado del Proyecto

Genera una visualización gráfica del estado del proyecto con el siguiente código:

```python
# Visualizar el estado del proyecto
visualize.plot_task_status(mi_proyecto)
```

## Ejemplos

```python
from proyecto_gestor import Project, visualize

# Crear un nuevo proyecto
mi_proyecto = Project("Proyecto de Ejemplo")

# Agregar tareas al proyecto
tarea1 = mi_proyecto.add_task("Tarea 1", "Juan", "2023-11-01", "2023-11-15", 3, 2)
tarea2 = mi_proyecto.add_task("Tarea 2", "María", "2023-11-05", "2023-11-20", 2, 1)

# Actualizar tareas en el proyecto
mi_proyecto.update_task("Tarea 1", responsible="Ana", completed=True)
mi_proyecto.update_task("Tarea 2", importance=1)

# Visualizar el estado del proyecto
visualize.plot_task_status(mi_proyecto)
```

---
Unax Barrainkua y Gorka Escalante