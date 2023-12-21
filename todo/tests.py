from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer
from django.urls import reverse


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        CustomUser = get_user_model()
        testuser = CustomUser.objects.create_user(username="testuser", password="12345")
        tag1 = Tag.objects.create(name="tag1", user=testuser)
        Tag.objects.create(name="tag2", user=testuser)
        todo = Todo.objects.create(title="Test Todo", user=testuser)
        todo.tags.add(tag1)

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

    from django.utils import timezone

    def test_todo_serializer(self):
        todo = Todo.objects.get(id=1)
        serializer = TodoSerializer(todo)
        self.assertEqual(
            serializer.data,
            {
                "id": 1,
                "title": "Test Todo",
                "description": "",
                "completed": False,
                "created_at": todo.created_at.isoformat().replace("+00:00", "Z"),
                "updated_at": todo.updated_at.isoformat().replace("+00:00", "Z"),
                "due_date": None,
                "priority": "M",
                "tags": ["tag1"],
                "user": "testuser",
            },
        )

    def test_tag_serializer(self):
        tag = Tag.objects.get(id=1)
        serializer = TagSerializer(tag)
        self.assertEqual(
            serializer.data,
            {
                "id": 1,
                "name": "tag1",
                "user": "testuser",
            },
        )


class TodoIntegrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        cls.todo = Todo.objects.create(title="Test Todo", user=cls.user)
        tag1 = Tag.objects.create(name="tag1", user=cls.user)
        cls.todo.tags.add(tag1)

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="testpass")

    def test_get_todos(self):
        response = self.client.get(reverse("todo-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["title"], "Test Todo")

    def test_create_todo(self):
        response = self.client.post(reverse("todo-list"), {"title": "New Todo"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 2)
        self.assertEqual(Todo.objects.latest("created_at").title, "New Todo")


class TagIntegrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="testpass")

    def test_get_tags(self):
        Tag.objects.create(name="Existing Tag", user=self.user)
        response = self.client.get(reverse("tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "Existing Tag")

    def test_create_tag(self):
        response = self.client.post(reverse("tag-list"), {"name": "New Tag"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.latest("id").name, "New Tag")


class TodoFilterIntegrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="testpass")
        Todo.objects.all().delete()

    def test_filter_todos_by_description(self):
        Todo.objects.create(
            title="Test Todo 1", description="Description 1", user=self.user
        )
        Todo.objects.create(
            title="Test Todo 2", description="Description 2", user=self.user
        )
        response = self.client.get(
            reverse("todo-list"), {"description": "Description 1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["title"], "Test Todo 1")
