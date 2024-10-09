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




class CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLesson
        fields = ['title','course_module']

class CourseModuleSerializer(serializers.ModelSerializer):
    course_lesson = CourseLessonSerializer(many=True,read_only=True,source='course_lessons')
    class Meta:
        model = CourseModule
        fields = ['title','course','course_lesson']



class MentorWorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorWorkPlace
        fields = ['logo','mentor']




class MentorSerializer(serializers.ModelSerializer):
    mentor_work_place = MentorWorkPlaceSerializer(many = True,read_only=True,source='mentor_work_places')
    class Meta:
        model = Mentor
        fields = ['full_name','profession','position','image','experience','course','mentor_work_place']

class OurProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProgram
        fields = ['log','title','description']

class OurProgramInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurProgramInfo
        fields = ['description','our_program','order']


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




# class MentorDetailSerializer(serializers.ModelSerializer):
#     mentor_achievments = MentorAchievementsSerializer(many = True, read_only=True)
#     mentor_work_places = MentorWorkPlaceSerializer(many = True,read_only=True)

#     class Meta:
#         model = Mentor
#         fields = ['full_name','profession','position','image','experience','mentor_achievments','mentor_workplaces']


class CourseDetailSerializer(serializers.ModelSerializer):
    for_whom = ForWhomSerializer(many=True,read_only=True,source='for_whoms')
    course_plan = CoursePlanSerializer(many=True,read_only=True,source='course_plans')
    course_module = CourseModuleSerializer(many = True,read_only=True,source='course_modules')
    mentor = MentorSerializer(many = True, read_only=True,source='mentors')
    computer_feature = ComputerFeaturesSerializer(many = True,read_only=True,source='computer_features')

    

# 'for_whom','course_plan','course_modules','mentor','computer_features'
    class Meta:
        model = Course
        fields = ['title','description','mentor','for_whom','course_plan','course_module','computer_feature']
