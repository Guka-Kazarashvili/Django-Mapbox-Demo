from django.urls import path
from .views import AddressView, delete_address

urlpatterns = [
    path('', AddressView.as_view(), name='home'),
    path('delete-address/<int:address_id>/', delete_address, name='delete_address'),
]