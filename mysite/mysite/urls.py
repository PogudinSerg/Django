from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainApp.urls')),
    path('webexample/', include('webexample.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
