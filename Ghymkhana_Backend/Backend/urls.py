from django.urls import path
from . import views
urlpatterns = [
    path('meeting/', views.getmeeting),
    path('ugsenator/', views.getugSenator),
    path('pgsenator/', views.getpgSenator),
    path('faculty/', views.getfacultyExecutivebodie),
    path('student/', views.getstudentExecutivebodie),
    path('upcomingevents/', views.getupComing),
    path('', views.home, name = 'home-page'),
    path('senate/',views.Senate,name='senate-page'),
    path('minutes/',views.minutes,name='minutes-page'),
]