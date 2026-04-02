from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='film_lista'),
    path('crea/', views.crea, name='film_crea'),
    path('<int:pk>/', views.dettaglio, name='film_dettaglio'),
    path('<int:pk>/modifica/', views.modifica, name='film_modifica'),
    path('<int:pk>/elimina/', views.elimina, name='film_elimina'),
]
