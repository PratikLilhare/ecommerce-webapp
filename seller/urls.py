from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.seller),
    path('add_product/',views.add_product)
]