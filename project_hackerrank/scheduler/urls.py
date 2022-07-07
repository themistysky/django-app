from django.urls import path
from . import views

urlpatterns = [
    path('class/', views.class_, name='class_'),
    path('class/<id>', views.class_id, name='class_id'),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher/<id>', views.teacher_id, name='teacher_id'),
    path('generate/', views.generate, name='generate')
]
