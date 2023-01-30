from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), # homepage
    path('post/<str:pk>', views.post, name = 'post') # when you click on a post in index.html
]