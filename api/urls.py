from django.urls import path
from . import views

urlpatterns = [
    path('zoho_create_child_account/', views.create_account, name='create_account'),
    path('zoho_update_customer/', views.update_customer, name='update_customer'),
    path('zoho_update_invoice/', views.update_invoice, name='update_invoice'),
    path('zoho_update_products/', views.update_products, name='update_products'),
]
