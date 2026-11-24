"""Модуль ядра Task Tracker для лабораторной работы 4."""


class Task:
    def __init__(self, task_id, title, status="New"):
        self.task_id = task_id
        self.title = title
        self.status = status

    def to_dict(self):
        return {"id": self.task_id, "title": self.title, "status": self.status}


class TaskTracker:
    ALLOWED_STATUSES = ["New", "Approved", "Committed", "QA", "Done"]

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def create_task(self, title):
        if not title or not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        task = Task(self._next_id, title.strip())
        self._tasks[task.task_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id):
        if task_id not in self._tasks:
            raise KeyError(f"Задача {task_id} не найдена")
        return self._tasks[task_id]

    def update_status(self, task_id, status):
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(f"Неизвестный статус: {status}")
        task = self.get_task(task_id)
        task.status = status
        return task

    def delete_task(self, task_id):
        self.get_task(task_id)
        del self._tasks[task_id]

    def list_tasks(self, status=None):
        tasks = list(self._tasks.values())
        if status:
            tasks = [t for t in tasks if t.status == status]
        return tasks
