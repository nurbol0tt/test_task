from django.urls import reverse_lazy
from django.views import generic

from user.forms import SignUpForm


class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy('login')
