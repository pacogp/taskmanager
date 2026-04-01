import json
from pathlib import Path

from task_manager import TaskManager


def create_manager(tmp_path: Path) -> TaskManager:
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    return TaskManager()


def read_saved_tasks(file_path: Path) -> list[dict]:
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def test_add_task_persists_task_and_increments_id(tmp_path, capsys):
    manager = create_manager(tmp_path)

    manager.add_task("Preparar presentación")

    captured = capsys.readouterr()
    saved_tasks = read_saved_tasks(tmp_path / "tasks.json")

    assert "Task added" in captured.out
    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 1
    assert manager._tasks[0].description == "Preparar presentación"
    assert manager._next_id == 2
    assert saved_tasks == [
        {"id": 1, "description": "Preparar presentación", "completed": False}
    ]


def test_complete_task_marks_task_as_completed_and_saves(tmp_path, capsys):
    manager = create_manager(tmp_path)
    manager.add_task("Revisar correo")
    capsys.readouterr()

    manager.complete_tasks(1)

    captured = capsys.readouterr()
    saved_tasks = read_saved_tasks(tmp_path / "tasks.json")

    assert "Task completed" in captured.out
    assert manager._tasks[0].completed is True
    assert saved_tasks[0]["completed"] is True


def test_delete_task_removes_task_and_updates_file(tmp_path, capsys):
    manager = create_manager(tmp_path)
    manager.add_task("Tarea 1")
    manager.add_task("Tarea 2")
    capsys.readouterr()

    manager.delete_task(1)

    captured = capsys.readouterr()
    saved_tasks = read_saved_tasks(tmp_path / "tasks.json")

    assert "Task deleted" in captured.out
    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 2
    assert saved_tasks == [{"id": 2, "description": "Tarea 2", "completed": False}]


def test_load_tasks_recovers_existing_tasks_and_next_id(tmp_path):
    task_file = tmp_path / "tasks.json"
    task_file.write_text(
        json.dumps(
            [
                {"id": 1, "description": "Primera", "completed": False},
                {"id": 2, "description": "Segunda", "completed": True},
            ]
        ),
        encoding="utf-8",
    )

    manager = create_manager(tmp_path)

    assert len(manager._tasks) == 2
    assert manager._tasks[1].description == "Segunda"
    assert manager._tasks[1].completed is True
    assert manager._next_id == 3


def test_list_task_shows_empty_message_when_no_tasks(tmp_path, capsys):
    manager = create_manager(tmp_path)

    manager.list_task()

    captured = capsys.readouterr()
    assert "No tasks available." in captured.out