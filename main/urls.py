from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('timer/', views.timer, name='timer'),
    path('shedule/', views.schedule, name='schedule'),
    path('progress/', views.progress, name="progress"),
]