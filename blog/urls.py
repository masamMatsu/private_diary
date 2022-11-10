from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.TopView.as_view(), name="top"),
    path('post/', views.PostView.as_view(), name="post"),
]
