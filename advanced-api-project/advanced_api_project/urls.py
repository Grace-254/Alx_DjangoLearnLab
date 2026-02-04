from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Expose book API under /books/...
    path("", include("api.urls")),
]
