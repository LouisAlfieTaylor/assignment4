import pytest
from app.logic_layer import TaskManager


@pytest.fixture
def db_config():
    return {
        "host": "localhost",
        "user": "root",
        "password": "root123",
        "database": "tasklist_assignment4"
    }

@pytest.fixture
def task_manager(db_config):
    tm = TaskManager(db_config)
    yield tm
    tm.close()

def test_add_task(task_manager):
    task_id = task_manager.add_task("Sample Task")
    tasks = task_manager.load_tasks()
    assert any(t["id"] == task_id and t["task_text"] == "Sample Task" for t in tasks)

def test_update_task(task_manager):
    task_id = task_manager.add_task("Old Text")
    task_manager.update_task("New Text", task_id)
    tasks = task_manager.load_tasks()
    assert any(t["id"] == task_id and t["task_text"] == "New Text" for t in tasks)

def test_delete_task(task_manager):
    task_id = task_manager.add_task("Temp Task")
    task_manager.delete_task(task_id)
    tasks = task_manager.load_tasks()
    assert all(t["id"] != task_id for t in tasks)
