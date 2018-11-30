# posts/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.LocationReport.as_view({'get': 'list'})),
    url('', views.UserInteraction.as_view({'get': 'list'})),
    url('', views.MoodReport.as_view({'get': 'list'})),
    url('', views.ThoughtDistortionReport.as_view({'get': 'list'})),
    # url('<int:pk>/', views.MoodTypeDetail.as_view({'get': 'list'})),
]
