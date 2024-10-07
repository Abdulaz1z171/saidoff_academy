from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from .translation import *


# Register your models here.


class OurProgramTranslationAdmin(TranslationAdmin):
    list_display = ('title',)

admin.site.register(OurProgram,OurProgramTranslationAdmin)


class OurProgramInfoTranslationAdmin(TranslationAdmin):
    list_display = ('description',)

admin.site.register(OurProgramInfo,OurProgramInfoTranslationAdmin)

class FeedbackTranslationAdmin(TranslationAdmin):
    pass

admin.site.register(Feedback,FeedbackTranslationAdmin)

class FAQTranslationAdmin(TranslationAdmin):
    list_display = ('question',)

admin.site.register(FAQ,FAQTranslationAdmin)

class WhyUsTranslationAdmin(TranslationAdmin):
    list_display = ('title',)

admin.site.register(WhyUs,WhyUsTranslationAdmin)



for a in [Course,ForWhom,CourseLesson,CourseModule,CoursePlan,ComputerFeatures,UserContactAplication,Mentor,MentorAchievements,MentorWorkPlace,Partner]:
    admin.site.register(a)