from django.contrib import admin
from django.urls import path, re_path
from app_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/$',views.app_api_list),
    #re_path(r'^api/app_api/(?P<pk>[0-9]+)',views.app_api_detail),
]
