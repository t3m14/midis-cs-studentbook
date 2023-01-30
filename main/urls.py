from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theme/<str:slug>/', views.theme_view, name='theme'),
    path('theme/<str:slug>/<str:option>', views.theme_view, name='theme'),
]