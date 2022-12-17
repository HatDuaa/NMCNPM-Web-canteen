from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.DishListView.as_view()),
   path('register/', views.register, name='register'),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
   path('<int:pk>/', views.DishView),
   # path('buy_dish/<int:dish_id>/', views.buy_dish, name='buy_dish'),
]
