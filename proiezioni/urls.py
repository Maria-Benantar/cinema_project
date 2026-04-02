from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='proiezioni_lista'),
    path('crea/', views.crea, name='proiezioni_crea'),
    path('<int:pk>/', views.dettaglio, name='proiezioni_dettaglio'),
    path('<int:pk>/modifica/', views.modifica, name='proiezioni_modifica'),
    path('<int:pk>/elimina/', views.elimina, name='proiezioni_elimina'),
]
