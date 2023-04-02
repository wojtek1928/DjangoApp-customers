from django.urls import path
from . import views

urlpatterns = [
    # API paths
    path('', views.CustomersList.as_view(), name='customers-add-list-api'),
    path('<uuid:id>', views.CustomerDetail.as_view(),
         name='customer-deatail-api'),
]
