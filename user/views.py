from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LoginView(TemplateView):
    template_name = "user/login.html"


class RegisterView(TemplateView):
    template_name = "user/register.html"