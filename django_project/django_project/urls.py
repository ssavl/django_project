"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('archive/articles', views.articles_view),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:id>/', views.article_detail),
    path('<int:pk>/', views.article_id),
    path('', views.start),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('my_app.urls')),
    path('users/', include('app_users.urls'), name='users'),

]
