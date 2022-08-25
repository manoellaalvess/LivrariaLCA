from django.urls import path
from .views import LivroCreate, LivroUpdate
from .views import LivroDelete
from .views import LivroList, LivroAdm

urlpatterns = [
    path('cadastrar/livro', LivroCreate.as_view(), name='cadastrar-campo'),
    
    path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name = 'editar-livro'),

    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name = 'excluir-livro'),

    path('listar/livros/', LivroList.as_view(), name = 'listar/livros'),

    path('listar/livroadm', LivroAdm.as_view(), name='listar/adm'),

]