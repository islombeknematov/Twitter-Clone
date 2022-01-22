from modeltranslation.translator import register, TranslationOptions
from social.models import *


@register(PostModel)
class PostModelTranslationOptions(TranslationOptions):
    fields = ('body',)

