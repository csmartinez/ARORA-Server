# posts/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.Quest.as_view({'get': 'list'})),
    # url('<int:pk>/', views.MoodTypeDetail.as_view({'get': 'list'})),
]
