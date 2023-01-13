from django.urls import path
from . import views
urlpatterns = [
    path('meeting/', views.getmeeting),
    path('ugsenator/', views.getugSenator),
    path('pgsenator/', views.getpgSenator),
    path('faculty/', views.getfacultyExecutivebodie),
    path('student/', views.getstudentExecutivebodie),
]