from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myblog.urls")),
    path('postlist_client/', include('postlist_client.urls')),
    path('postlist_admin/', include('postlist_admin.urls')),
    path('write/', include('write.urls')),
    path('post/', include('post.urls')),
]