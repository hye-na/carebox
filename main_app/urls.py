from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('products/', views.product_view, name='products'),
    path('products/<int:product_id>', views.product_detail, name='product_detail')
    # path('products/', views.ProductListView.as_view(), names='products'),
]
