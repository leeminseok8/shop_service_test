from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Shop_Service API",
        default_version="v0.1",
        description="Shop_Service API 문서",
        terms_of_service="https://github.com/leeminseok8/shop_service_test",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("shop/products/", include("products.urls")),
    # swagger
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^doc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
