
from django.urls import path
from .views import ProductListView, ProductDetailView
from . import views
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<int:pk>/', ProductDetailView.as_view(), name='produit_detail'),
    # path('admin/main/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('ajax/load-communes/', views.load_communes, name='ajax_load_communes'),  # <-- this one here

]
