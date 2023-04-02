from rest_framework import generics, permissions

from customers.models import Customer
from .serializers import CustomerSerializer


# API Views
#################################################################
# API customer addition and customers list view
class CustomersList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.all()


# API customer details
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Customer.objects.all()
    lookup_field = 'id'
