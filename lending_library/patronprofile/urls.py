from django.conf.urls import url
from django.shortcuts import render
# from patronprofile.views import a_view
from books.models import Book
from django.views.generic import CreateView


def a_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'patronprofile/profile.html', context=context)

class CreateBook(CreateView):
    model = Book
    template_name = 'patronprofile/profile.html'
    fields = ['title', 'author', 'cover']


urlpatterns = [
    url('^profile$', a_view, name='a_profile'),
    url('^new_book$', CreateBook.as_view(), name='new-book')
]
