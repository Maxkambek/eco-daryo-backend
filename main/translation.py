from modeltranslation.translator import register, TranslationOptions
from .models import Slider, News, Video, Links, Leaders, RegionUnit, LegalDocs


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Links)
class LinksTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Leaders)
class LeadersTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'work_time')


@register(LegalDocs)
class LegalDocsTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(RegionUnit)
class RegionUnitTranslationOptions(TranslationOptions):
    fields = (
        'name', 'position', 'work_time', 'place_birth', 'specialty', 'nationality', 'party', 'malumoti', 'tamomlagan',
        'ilmiy_daraja', 'ilmiy_unvon', 'language', 'davlat_mukofoti', 'xald_deputatlari')
