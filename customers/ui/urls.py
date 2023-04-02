from django.urls import path
from . import views

# UI paths
urlpatterns = [
    path('', views.customer_add_list_view, name='customers-add-list-ui'),
    path('<uuid:id>/edit',
         views.customer_edit, name='customer-edit-ui'),
    path('<uuid:id>/delete',
         views.customer_delete, name='customer-delete-ui'),
]
