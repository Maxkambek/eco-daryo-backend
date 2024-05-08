from django.urls import path
from . import views

urlpatterns = [
    path('slider/', views.SliderList.as_view()),
    path('news/', views.NewsList.as_view()),
    path('video/', views.VideoList.as_view()),
    path('links/', views.LinksList.as_view()),
    path('leaders/', views.LeaderList.as_view()),
    path('region/', views.RegionUnitList.as_view()),
    path('region/<int:pk>/', views.RegionUnitDetail.as_view()),
    path('legal/', views.LegalDocsList.as_view())
]
