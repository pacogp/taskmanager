# Task Manager

Aplicación de consola en Python para gestionar tareas personales. El proyecto permite crear, listar, completar y eliminar tareas, y además puede dividir tareas complejas en subtareas usando IA a través de OpenRouter.

## Tabla de contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías usadas](#tecnologías-usadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Persistencia de datos](#persistencia-de-datos)
- [Pruebas](#pruebas)
- [Dependencias](#dependencias)
- [Limitaciones actuales](#limitaciones-actuales)
- [Mejoras recomendadas](#mejoras-recomendadas)

## Descripción

Este proyecto implementa un gestor de tareas en terminal con almacenamiento local en JSON. También incorpora una funcionalidad opcional de IA que transforma una tarea compleja en varias subtareas accionables.

Es un proyecto adecuado para practicar:

- programación orientada a objetos en Python
- lectura y escritura de archivos JSON
- interacción por consola
- integración con APIs externas
- pruebas automáticas con `pytest`

## Características

- Añadir tareas simples.
- Listar tareas guardadas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Guardado automático en `tasks.json`.
- Generación de subtareas mediante IA.
- Pruebas automáticas para la lógica principal.

## Tecnologías usadas

- Python
- JSON para persistencia local
- `openai` para consumir OpenRouter
- `python-dotenv` para variables de entorno
- `pytest` para testing

## Estructura del proyecto

```text
proyecto_TaskManager/
├── ai_service.py
├── main.py
├── README.md
├── requerements.txt
├── task_manager.py
├── tasks.json
└── test_task_manager.py
```

### Descripción de archivos

- `main.py`: punto de entrada y menú interactivo.
- `task_manager.py`: lógica de negocio del gestor de tareas.
- `ai_service.py`: integración con OpenRouter para generar subtareas.
- `tasks.json`: archivo de almacenamiento persistente.
- `test_task_manager.py`: pruebas automáticas de las funciones principales.
- `requerements.txt`: lista de dependencias del proyecto.

## Requisitos

- Python 3.10 o superior.
- `pip` instalado.
- Cuenta y clave API de OpenRouter para usar la opción de tareas complejas.

## Instalación

1. Clona o descarga este repositorio.
2. Abre una terminal en la raíz del proyecto.
3. Crea un entorno virtual:

	 ```powershell
	 python -m venv .venv
	 ```

4. Activa el entorno virtual:

	 ```powershell
	 .venv\Scripts\Activate.ps1
	 ```

5. Instala las dependencias:

	 ```powershell
	 pip install -r requerements.txt
	 ```

## Configuración

Para habilitar la funcionalidad de IA, crea un archivo `.env` en la raíz del proyecto. Puedes apoyarte en el archivo de ejemplo `.env.example`:

```env
OPENROUTER_API_KEY=tu_clave_aqui
```

### Notas sobre la IA

- Si no existe `OPENROUTER_API_KEY`, la aplicación seguirá funcionando para las tareas normales.
- Si la clave no está configurada, la opción de tarea compleja devolverá un mensaje de error controlado.
- Si se supera el límite de peticiones, se mostrará un error indicando el problema de cuota o rate limit.

## Uso

Ejecuta la aplicación con:

```powershell
python main.py
```

### Menú principal

1. Agregar tarea
2. Agregar tarea compleja
3. Listar tareas
4. Marcar tarea como completada
5. Eliminar tarea
6. Salir

### Ejemplo de flujo de uso

1. Inicias la aplicación.
2. Seleccionas la opción para crear una tarea.
3. Introduces una descripción.
4. El sistema guarda la tarea automáticamente.
5. Puedes listar las tareas, completarlas o eliminarlas.

### Ejemplo de tarea compleja

Si introduces una tarea como:

`Preparar una presentación para el cliente`

La IA puede generar subtareas como:

- Definir el objetivo de la presentación
- Recopilar la información necesaria
- Diseñar las diapositivas
- Revisar el contenido final

## Persistencia de datos

Las tareas se almacenan automáticamente en `tasks.json`.

Cada tarea se guarda con esta estructura:

```json
[
	{
		"id": 1,
		"description": "Preparar informe",
		"completed": false
	}
]
```

## Pruebas

El proyecto incluye pruebas automáticas para las funcionalidades principales de `TaskManager`.

### Casos cubiertos

- creación de tareas
- guardado en archivo JSON
- marcado de tarea como completada
- eliminación de tareas
- carga de tareas existentes
- comportamiento al listar cuando no hay tareas

### Ejecutar tests

Si no tienes `pytest` instalado:

```powershell
pip install pytest
```

Para ejecutar las pruebas:

```powershell
pytest test_task_manager.py
```

## Dependencias

Dependencias registradas en `requerements.txt`:

- `certifi`
- `charset-normalizer`
- `idna`
- `requests`
- `urllib3`
- `python-dotenv`
- `openai`

## Limitaciones actuales

- La interfaz es solo de consola.
- El proyecto mezcla mensajes en español e inglés.
- El método `Task.__str__` no muestra explícitamente si la tarea está completada.
- El archivo de dependencias está nombrado como `requerements.txt` en lugar de `requirements.txt`.
- Los tests están en la raíz del proyecto en lugar de una carpeta dedicada.

## Mejoras recomendadas

### Mejoras funcionales

- Añadir edición de tareas.
- Añadir filtros por estado.
- Añadir búsqueda por texto.
- Confirmar antes de eliminar una tarea.

### Mejoras de código

- Renombrar `requerements.txt` a `requirements.txt`.
- Unificar el idioma de todos los mensajes.
- Mejorar el método `__str__` para mostrar el estado.
- Renombrar métodos como `list_task` y `complete_tasks` para que sean más consistentes.

### Mejoras de estructura

- Mover los tests a una carpeta `tests/`.
- Añadir `requirements-dev.txt` para dependencias de desarrollo.
- Añadir integración continua con GitHub Actions.

## Estado actual del proyecto

Actualmente el proyecto ya dispone de pruebas automáticas para las funcionalidades principales y de documentación básica para instalación, uso y configuración.
 