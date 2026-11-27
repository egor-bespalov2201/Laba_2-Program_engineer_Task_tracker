"""Автотесты для ядра Task Tracker."""
import unittest

from task_tracker import TaskTracker


class TestTaskTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = TaskTracker()

    def test_create_task(self):
        task = self.tracker.create_task("Создать контроллер")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.status, "New")
        print("Тест создания задачи пройден: ID=1, статус=New")

    def test_create_empty_title_raises(self):
        with self.assertRaises(ValueError):
            self.tracker.create_task("   ")
        print("Тест пустого названия пройден: ValueError корректно вызван")

    def test_update_status(self):
        task = self.tracker.create_task("Написать тесты")
        self.tracker.update_status(task.task_id, "Committed")
        self.assertEqual(self.tracker.get_task(task.task_id).status, "Committed")
        print("Тест обновления статуса пройден: статус изменён на Committed")

    def test_update_invalid_status_raises(self):
        task = self.tracker.create_task("Написать тесты")
        with self.assertRaises(ValueError):
            self.tracker.update_status(task.task_id, "Неизвестный")
        print("Тест неверного статуса пройден: ValueError корректно вызван")

    def test_delete_task(self):
        task = self.tracker.create_task("Временная задача")
        self.tracker.delete_task(task.task_id)
        self.assertEqual(len(self.tracker.list_tasks()), 0)
        print("Тест удаления задачи пройден: список задач пуст")

    def test_filter_by_status(self):
        t1 = self.tracker.create_task("Первая")
        self.tracker.create_task("Вторая")
        self.tracker.update_status(t1.task_id, "Done")
        done = self.tracker.list_tasks(status="Done")
        self.assertEqual(len(done), 1)
        self.assertEqual(done[0].title, "Первая")
        print("Тест фильтрации по статусу пройден: найдена 1 задача со статусом Done")


if __name__ == "__main__":
    unittest.main()
