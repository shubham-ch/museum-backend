from django.urls import path
from django.urls.conf import include
from django.urls import re_path
from django.conf.urls import url
from users import urls as auth_urls
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from watchman.views import status
import os
from fileServers import urls as FileServerUrls
from fileServers.views import ServeFile

urlpatterns = [
    # DEV_EASE_UP: TO BE DELETED
    path("api/health", status, name="health-view"),
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("auth/", include(auth_urls)),
    path("files/",include(FileServerUrls)),
    url(r"^media/(?P<path>.*)$", ServeFile.as_view()),
]

if os.getenv("LOCAL_DEVELOPMENT", None) is not None:
    from django.contrib import admin
    urlpatterns.append(path("admin", admin.site.urls))