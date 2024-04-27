from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('api/destinations/create/', DestinationCreateView.as_view(), name='destination-create'),
    path('destinations/<int:pk>/', DestinationRetrieveView.as_view(), name='destination-retrieve'),
    path('api/destinations/<int:pk>/update/', DestinationUpdateView.as_view(), name='destination-update'),
    path('destinations/<int:pk>/delete/', DestinationDestroyView.as_view(), name='destination-delete'),
    path('search/', DestinationSearchView.as_view(), name='destination-search'),

    path('create', views.createDestination, name='create'),
    path('read', views.display_destinations, name='showcase'),
    path('destinations/<int:pk>/update/', views.update_destination)
]