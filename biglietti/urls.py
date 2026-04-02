from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='biglietti_lista'),
    path('<int:pk>/', views.dettaglio, name='biglietti_dettaglio'),
    path('<int:pk>/vendi/', views.vendi, name='biglietti_vendi'),
    path('<int:pk>/libera/', views.libera, name='biglietti_libera'),
]
