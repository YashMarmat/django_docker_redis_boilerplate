from django.urls import path
from . import views


urlpatterns = [
    path('page2/', views.second_page_view, name='page2'),
    path('', views.homepage_view, name='home'),
]