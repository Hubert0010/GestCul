from django.urls import path
from. import views

urlpatterns = [
    path('membres/', views.list_membres, name= "list_membres"),
    path('form/',views.form_membres,name="form_membres"),
    path("add/", views.add_membre, name="add_membre")
]