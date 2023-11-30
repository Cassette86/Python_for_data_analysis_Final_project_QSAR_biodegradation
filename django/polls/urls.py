from django.urls import path

from . import views

urlpatterns = [
    path("", views.Accueil, name="index"),
    path("page1", views.info_data, name="index"),

    path("page2", views.visualization, name="index"),
    path('apply_Model', views.index_visualization, name='index'),

    path("page3", views.modeling, name="index"),
    path('apply_Model2', views.index_modeling, name='index'),

]
