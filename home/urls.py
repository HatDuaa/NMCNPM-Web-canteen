from django.urls import path
from . import views

urlpatterns = [
   path('', views.DishListView.as_view()),
   path('register/', views.register, name='register'),

]
