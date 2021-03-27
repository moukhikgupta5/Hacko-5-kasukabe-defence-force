from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Top Education Admin"
admin.site.site_title = "Top Education Admin Portal"
admin.site.index_title = "Welcome to Top Education"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]
