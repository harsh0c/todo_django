from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskViewTests(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            due_date='2024-12-31',
            priority='Medium',
            completed=False
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_list.html')
        self.assertContains(response, 'Test Task') # contains the title of the test task

    def test_add_task_view(self):
        response = self.client.post(reverse('add_task'), {
            'title': 'New Task',
            'description': 'A new task description',
            'due_date': '2024-12-31',
            'priority': 'High',
            'completed': 'on'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists()) 

    def test_edit_task_view(self):
        response = self.client.post(reverse('edit_task', args=[self.task.id]), {
            'title': 'Updated Task',
            'description': 'Updated description',
            'due_date': '2025-01-01',
            'priority': 'Low',
            'completed': 'off'
        })
        self.task.refresh_from_db() # Refresh task from database
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertFalse(self.task.completed)

    def test_delete_task_view(self):
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())  # Task should be deleted

    def test_delete_all_tasks_view(self):
        Task.objects.create(title='Another Task')  # Add another task
        response = self.client.post(reverse('delete_all_tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)  # All tasks should be deleted
