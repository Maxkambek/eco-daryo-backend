from rest_framework import generics
from .models import Slider, News, Video, Links, Leaders, RegionUnit, LegalDocs
from .serializers import SliderSerializer, NewsSerializer, VideoSerializer, LinksSerializer, RegionUnitSerializer, \
    LegalDocsSerializer, LeadersSerializer


class SliderList(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class LeaderList(generics.ListAPIView):
    queryset = Leaders.objects.all()
    serializer_class = LeadersSerializer


class LinksList(generics.ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class RegionUnitList(generics.ListAPIView):
    queryset = RegionUnit.objects.all()
    serializer_class = RegionUnitSerializer


class RegionUnitDetail(generics.RetrieveAPIView):
    queryset = RegionUnit.objects.all()
    serializer_class = RegionUnitSerializer


class LegalDocsList(generics.ListAPIView):
    queryset = LegalDocs.objects.all()
    serializer_class = LegalDocsSerializer
