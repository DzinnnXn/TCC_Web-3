from django.urls import path
from . import views
from .views import buscar_itens

urlpatterns = [
        path('', views.homepage, name="homepage"),         # Inclui as urls do app blog
        path('homepageDark', views.homepageDark, name="homepageDark"),   # Inclui as urls do app blog
        path('login', views.login, name="login"),           # Inclui as urls do app blog
        path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
        path('profile', views.profile, name="profile"),       # Inclui as urls do app blog
        path('faq', views.faq, name="faq"),                 # Inclui as urls do app blog
        path('welcomeHomepage', views.welcomeHomepage, name="welcomeHomepage"),   # Inclui as urls do app blog
        path('itens', views.itens, name="itens"),           # Inclui as urls do app blog
        path('adicionar_inventario', views.adicionar_inventario, name="adicionar_inventario"),   # Inclui as urls do app blog
        path('buscar', buscar_itens, name='buscar_itens'), 
        path('excluir_inventario', views.excluir_inventario, name='excluir_inventario'),

]