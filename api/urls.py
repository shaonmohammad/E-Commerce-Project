from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    CategoryListView, CategoryCreateView, CategoryDetailView,
    ProductListView, ProductCreateView, ProductDetailView,
    StockListView, StockCreateView, StockDetailView,RegistrationView
)

urlpatterns = [
    # Authentication API
    path('register/',RegistrationView.as_view(),name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   

     # Category endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Product endpoints
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Stock endpoints
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('stocks/create/', StockCreateView.as_view(), name='stock-create'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
]
