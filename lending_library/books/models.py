from django.db import models
import uuid

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.UUIDField(default=uuid.uuid4, editable=False)

    def __repr__(self):
        return "<Book: {}>".format(self.title)