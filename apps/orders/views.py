from django.shortcuts import render
from rest_framework import generics

from apps.users.mixins import CustomLoginRequiredMixin
from .serializers import OrderListSerializer, OrderSerializer, OrderAddSerializer
from .models import Order

class OrderList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.order_by('-id').filter(user = request.login_user.id)
        return self.list(request, *args, **kwargs)

class OrderAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderAddSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.login_user.id
        return super().create(request, *args, **kwargs)
    


class OrderHistoryAPIView(CustomLoginRequiredMixin, generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        print(self.request.login_user)
        user_id = self.request.login_user  # Assuming you are using authentication
        return Order.objects.filter(user_id=user_id)