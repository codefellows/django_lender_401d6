from django.conf.urls import url
from django.shortcuts import render
# from patronprofile.views import a_view

def a_view(request):
    return render(request, 'lending_library/home.html')

urlpatterns = [
    url('^profile$', a_view, name='a_profile')
]
