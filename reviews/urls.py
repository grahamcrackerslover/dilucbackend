from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_review),
    path('get/', views.list_reviews),
    path('stats/', views.reviews_stats)
]