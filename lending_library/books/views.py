from django.shortcuts import render


# Create your views here.

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    slug_url_kwarg = 'username'