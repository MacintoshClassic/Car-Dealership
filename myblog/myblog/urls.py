from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("CarDealership/", include("CarDealership.urls")),
    # added as default page
    path("", include("CarDealership.urls")),
    path("admin/", admin.site.urls),
]
