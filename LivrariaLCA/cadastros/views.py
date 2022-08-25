from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Livro
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from rest_framework.permissions import IsAuthenticated

#CREATE
class LivroCreate(IsAuthenticated, CreateView):
    permission_classes = (IsAuthenticated)
    model = Livro
    fields = ['titulo', 'autor', 'preco', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar/adm')


# UPDATE
class LivroUpdate(IsAuthenticated, UpdateView):
    permission_classes = (IsAuthenticated)
    model = Livro
    fields = ['titulo', 'autor', 'preco', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar/livros')


#DELETE
class LivroDelete(IsAuthenticated, DeleteView):
    permission_classes = (IsAuthenticated)
    model = Livro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar/adm')


#LISTVIEW
class LivroList(ListView):
    model = Livro
    template_name = 'cadastros/listar-livro.html'
    success_url = reverse_lazy('listar/livro')

class LivroAdm(IsAuthenticated, ListView):
    permission_classes = (IsAuthenticated)
    model = Livro
    template_name = 'cadastros/listar-livroadm.html'
    success_url = reverse_lazy('listar/adm')
