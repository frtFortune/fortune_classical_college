from django.test import SimpleTestCase

from .models import UserRole


class UserRoleTests(SimpleTestCase):
    def test_user_role_choices_exclude_parent(self):
        choices = dict(UserRole.choices)

        self.assertEqual(set(choices), {'admin', 'teacher', 'student'})
        self.assertNotIn('parent', choices)
