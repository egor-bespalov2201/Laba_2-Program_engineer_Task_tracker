"""Точка входа Task Tracker: демо-запуск проекта."""
import sys

from task_tracker import TaskTracker


def run_demo():
    tracker = TaskTracker()
    t1 = tracker.create_task("Разработка ядра системы")
    t2 = tracker.create_task("Реализация REST API")
    tracker.update_status(t1.task_id, "Committed")
    tracker.update_status(t2.task_id, "Done")
    print("=== Task Tracker запущен в демо-режиме ===")
    for task in tracker.list_tasks():
        print(f"  [{task.status}] {task.title}")
    print(f"Всего задач в системе: {len(tracker.list_tasks())}")
    print("=== Проект отработал успешно ===")
    return 0


if __name__ == "__main__":
    sys.exit(run_demo())
