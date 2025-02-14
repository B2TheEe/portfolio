from modeltranslation.translator import register, TranslationOptions
from .models import BlogArticle

@register(BlogArticle)
class BlogArticleTranslationOptions(TranslationOptions):
    fields = ( 'title', 'text', ,)