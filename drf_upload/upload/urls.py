from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('', views.PostView.as_view(), name='test'),
]
