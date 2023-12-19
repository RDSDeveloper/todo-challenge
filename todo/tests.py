from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Todo, Tag


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Tag.objects.create(name="tag1")
        Tag.objects.create(name="tag2")
        CustomUser = get_user_model()
        CustomUser.objects.create_user(username="testuser", password="12345")
        testuser = CustomUser.objects.get(id=1)
        Todo.objects.create(title="Test Todo", user=testuser)

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.title}"
        self.assertEquals(expected_object_name, "Test Todo")

    def test_todo_user(self):
        todo = Todo.objects.get(id=1)
        expected_todo_user = f"{todo.user.username}"
        self.assertEquals(expected_todo_user, "testuser")

    def test_tag_name(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = f"{tag.name}"
        self.assertEquals(expected_object_name, "tag1")
