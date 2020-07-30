from django.urls import path,include
from . import views

app_name="buyer"

urlpatterns = [
    path('',views.home),
    path('cart/<int:id>/', views.cart, name="cart"),
    path('view_cart/',views.view_cart, name = "view_cart"),
    path('category/<int:id>/', views.category),
    path('delete/<int:id>/',views.deleteProduct,name = "delete_product"),
    path('profile/',views.profile)
]
