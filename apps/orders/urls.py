from django.urls import path
from . import views

urlpatterns =[
    path('', views.OrderHistoryAPIView.as_view(), name='order-list'),
    path('add/', views.OrderAdd.as_view(), name='order-add')
]