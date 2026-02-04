from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Expose the Book endpoints under /books/ and /books/<pk>/
    path("", include("api.urls")),
]
