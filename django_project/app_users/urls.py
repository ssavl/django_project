from django.urls import path
from app_users.views import MyLogoutView, MyLoginView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

]