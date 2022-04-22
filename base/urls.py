from django.contrib.auth.views import LogoutView
from django.urls import path

import base.views

urlpatterns = [
    path('', base.views.SiteLoginView.as_view(), name='login'),
    path('login/', base.views.SiteLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('inicio/', base.views.HomeView.as_view(), name='home'),
    path('dashboard/', base.views.DashboardView.as_view(), name='admin-home'),
    # Cuotero
    path('cuotero/', base.views.CuoteroListView.as_view(), name='cuotero.list'),
    path('cuotero/<int:cuotero_id>/', base.views.CuoteroDetailView.as_view(), name='cuotero.detail'),
    path('cuotero/crear/', base.views.CuoteroCreateView.as_view(), name='cuotero.create'),
    path('cuotero/<int:cuotero_id>/editar/', base.views.CuoteroUpdateView.as_view(), name='cuotero.update'),
    path('cuotero/<int:cuotero_id>/eliminar/', base.views.CuoteroDeleteView.as_view(), name='cuotero.delete'),
]
