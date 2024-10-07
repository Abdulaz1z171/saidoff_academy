from modeltranslation.translator import TranslationOptions, translator
from .models import *



class OurProgramTranslation(TranslationOptions):
    fields = ('title','description')

class OurProgramInfoTranslation(TranslationOptions):
    fields = ('description',)

class FeedbackTranslation(TranslationOptions):
    fields = ('comment',)

class FAQTranslation(TranslationOptions):
    fields = ('question','answer')

class WhyUsTranslation(TranslationOptions):
    fields = ('title','description')


for a,b in [(OurProgram,OurProgramTranslation),(Feedback,FeedbackTranslation),(FAQ,FAQTranslation),(WhyUs,WhyUsTranslation),(OurProgramInfo,OurProgramInfoTranslation)]:
    translator.register(a,b)