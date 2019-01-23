from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    path('', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('export/',views.export,name='export'),


]
