from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),

]
