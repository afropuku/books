from django.urls import path
from app import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<str:isbn>', views.DetailView.as_view(), name='detail'),
]
