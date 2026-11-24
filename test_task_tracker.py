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

    def test_create_empty_title_raises(self):
        with self.assertRaises(ValueError):
            self.tracker.create_task("   ")

    def test_update_status(self):
        task = self.tracker.create_task("Написать тесты")
        self.tracker.update_status(task.task_id, "Committed")
        self.assertEqual(self.tracker.get_task(task.task_id).status, "Committed")

    def test_update_invalid_status_raises(self):
        task = self.tracker.create_task("Написать тесты")
        with self.assertRaises(ValueError):
            self.tracker.update_status(task.task_id, "Неизвестный")

    def test_delete_task(self):
        task = self.tracker.create_task("Временная задача")
        self.tracker.delete_task(task.task_id)
        self.assertEqual(len(self.tracker.list_tasks()), 0)

    def test_filter_by_status(self):
        t1 = self.tracker.create_task("Первая")
        self.tracker.create_task("Вторая")
        self.tracker.update_status(t1.task_id, "Done")
        done = self.tracker.list_tasks(status="Done")
        self.assertEqual(len(done), 1)
        self.assertEqual(done[0].title, "Первая")


if __name__ == "__main__":
    unittest.main()
