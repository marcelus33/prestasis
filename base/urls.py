from django.contrib.auth.views import LogoutView
from django.urls import path

import base.views

urlpatterns = [
    path('', base.views.SiteLoginView.as_view(), name='login'),
    path('login/', base.views.SiteLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('inicio/', base.views.HomeView.as_view(), name='home'),
    path('dashboard/', base.views.DashboardView.as_view(), name='admin-home'),
]
