from django.urls import path, include
from .views import Todolist

urlpatterns = [
    path('list/', Todolist.as_view()),
]
