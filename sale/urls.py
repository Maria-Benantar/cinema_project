from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='sale_lista'),
    path('crea/', views.crea, name='sale_crea'),
    path('<int:pk>/', views.dettaglio, name='sale_dettaglio'),
    path('<int:pk>/modifica/', views.modifica, name='sale_modifica'),
    path('<int:pk>/elimina/', views.elimina, name='sale_elimina'),
]
