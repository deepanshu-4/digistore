from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.createpage, name="createpage"),
    path("randompage", views.random, name="random"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("editpage", views.editpage, name="editpage"),
    path("search", views.search, name="search")
]
