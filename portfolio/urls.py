from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('cards/', views.CardListView.as_view(), name='cards'),
    path('card/<int:pk>/', views.CardDetailView.as_view(), name='card'),
    path('illustrations/', views.IllustrationListView.as_view(), name='illustrations'),
    path('illustration/<int:pk>/', views.IllustrationDetailView.as_view(), name='illustration'),
    path('journals/', views.JournalListView.as_view(), name='journals'),
    path('journal/<int:pk>/', views.JournalDetailView.as_view(), name='journal'),
    path('packages/', views.PackageListView.as_view(), name='packages'),
    path('package/<int:pk>/', views.PackageDetailView.as_view(), name='package'),
    path('search_results', views.search_results, name='search-results'),
]
