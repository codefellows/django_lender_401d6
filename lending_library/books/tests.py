from django.test import TestCase, Client
from books.models import Book
import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
import os


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = factory.Sequence(lambda n: "book{}".format(n))
    author = factory.Sequence(lambda n: "person{}".format(n))
    cover = SimpleUploadedFile(
        name="foofile.jpg",
        content=open('/Users/nick/Downloads/malcolmx.jpg', 'rb').read(),
        content_type="image/jpeg"
    )

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class BookTests(TestCase):

    def setUp(self):
        books = [BookFactory.create() for i in range(20)]
        self.books = books
        self.client = Client()

    def tearDown(self):
        to_delete = os.path.join(BASE_DIR, 'book_covers', '*.jpg')
        os.system('rm -rf ' + to_delete)

    def test_some_route_lists_book_images(self):
        response = self.client.get(reverse('a_profile'))
