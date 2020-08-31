from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('article/<int:pk>/', views.article, name = 'article'),
    path('author/<int:pk>', views.author, name = 'author'),
    path('article/create/', views.create_article, name = 'create_article'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('register/', views.register, name = 'register')
]

