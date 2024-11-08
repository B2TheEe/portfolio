from modeltranslation.translator import register, TranslationOptions
from .models import AboutMe

@register(AboutMe)
class AboutMeranslationOptions(TranslationOptions):
    fields = ( 'about_me',)