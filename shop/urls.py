from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.list_items),
    path('buy/', views.buy_item)
]