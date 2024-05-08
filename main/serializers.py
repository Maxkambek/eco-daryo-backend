from rest_framework import serializers
from .models import Slider, News, Video, Links, Leaders, RegionUnit, LegalDocs


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'content', 'background_image']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'image', 'image_main', 'created_at']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file', 'created_at']


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'name', 'logo']


class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaders
        fields = ['id', 'name', 'image', 'position', 'phone', 'email', 'work_time']


class RegionUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionUnit
        fields = [
            'id',
            'name',
            'image',
            'position',
            'phone',
            'email',
            'work_time',
            'date_birth',
            'place_birth',
            'specialty',
            'nationality',
            'party',
            'malumoti',
            'tamomlagan',
            'ilmiy_daraja',
            'ilmiy_unvon',
            'language',
            'davlat_mukofoti',
            'xald_deputatlari'
        ]


class LegalDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDocs
        fields = ['id', 'name', 'link']
