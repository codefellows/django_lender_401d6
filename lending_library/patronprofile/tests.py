from django.test import TestCase
from django.contrib.auth.models import User
from patronprofile.models import PatronProfile

import factory
# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class ProfileTestCase(TestCase):
    """Tests for the profile model."""

    def setUp(self):
        users = [UserFactory.create() for i in range(20)]

        for user in users:
            user.set_password('foo')
            user.save()

        self.users = users

    def test_every_profile_must_have_a_user(self):
        """The name says it all."""

        with self.assertRaises(Exception):
            patron = PatronProfile()
            patron.save()

    def test_profile_with_user_prints_username(self):
        """."""
        some_profile = PatronProfile.objects.first()
        self.assertTrue(str(some_profile), some_profile.user.username)

    def test_new_user_has_a_profile(self):
        """."""
        user = UserFactory.create()
        profile = PatronProfile.objects.last()
        self.assertTrue(profile.user == user)

    def test_there_are_as_many_users_as_profile(self):
        """."""
        self.assertEquals(len(User.objects.all()), len(PatronProfile.objects.all()))
