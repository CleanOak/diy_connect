from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.PostList.as_view()),
]