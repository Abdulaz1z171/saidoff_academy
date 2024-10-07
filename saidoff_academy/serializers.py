from rest_framework import serializers
from .models import *


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title','description','image']


class ForWhomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForWhom
        fields = ['title','description','course']

class CoursePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePlan
        fields = ['total_duration','time_for_theory','time_for_practice','for_theory','for_practice','course']


class ComputerFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerFeatures
        fields = ['processor','cpu','video_card','screen','course']


class UserContactAplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactAplication
        fields = ['full_name','phone_number','is_checked','course']


class CourseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModule
        fields = ['title','course']

class CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLesson
        fields = ['title','course_module']

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['full_name','profession','position','image','experience']


class MentorWorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorWorkPlace
        fields = ['logo','mentor']


class MentorAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorAchievements
        fields = ['mentor','title']

class OurProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProgram
        fields = ['log','title','description']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['full_name','image','comment','profession']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['image']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question','answer']

class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ['image','title','description']
