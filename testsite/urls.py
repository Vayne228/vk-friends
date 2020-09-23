from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test,name="test_url"),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), name='logout'),
]
