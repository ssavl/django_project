from django.urls import path
from . import views


urlpatterns = [
    path('reporters/', views.ReporterListView.as_view()),
    path('articles/', views.ArticleListView.as_view()),
    path('articles/<int:year>', views.ArticleListViewYears.as_view()),
    path('reporters/<int:id>', views.ReporterListOfIdViews.as_view()),
]