from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView #novo video

#novo video
class IndexView(TemplateView):
    template_name = "index.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

class LoginView(TemplateView):
    template_name = 'login.html'
