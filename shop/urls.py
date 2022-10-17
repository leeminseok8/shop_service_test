from django.urls import path, include

urlpatterns = [
    path("shop/products/", include("products.urls")),
]
