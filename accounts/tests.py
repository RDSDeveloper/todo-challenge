from django.test import TestCase
from .models import CustomUser

class CustomUserTestCase(TestCase):
    """
    Test case for the CustomUser model.
    """

    def setUp(self):
        CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        CustomUser.objects.create_superuser(
            username="testadmin", password="testpass123", email="admin@test.com"
        )

    def test_custom_user_created(self):
        user = CustomUser.objects.get(username="testuser")
        self.assertEqual(user.username, "testuser")
        self.assertFalse(user.is_superuser)

    def test_custom_superuser_created(self):
        admin = CustomUser.objects.get(username="testadmin")
        self.assertEqual(admin.username, "testadmin")
        self.assertTrue(admin.is_superuser)