from modeltranslation.translator import register, TranslationOptions
from .models import AboutMe

@register(AboutMe)
class AboutMeranslationOptions(TranslationOptions):
    fields = ( 'photo','name','address','phone_number','email_address','github','linkedIn','about_me')