from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


# Create your views here.

class CourseView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


class ForWhomView(generics.ListAPIView):
    queryset = ForWhom.objects.all()
    serializer_class = ForWhomSerializer

class CoursePlanView(generics.ListAPIView):
    queryset = CoursePlan.objects.all()
    serializer_class = CoursePlanSerializer

class ComputerFeauturesView(generics.ListAPIView):
    queryset = ComputerFeatures.objects.all()
    serializer_class = ComputerFeaturesSerializer

class UserContactAplicationView(generics.ListCreateAPIView):
    queryset = UserContactAplication.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserContactAplicationSerializer


class CourseModuleView(generics.ListAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer

class CourseLessonView(generics.ListAPIView):
    queryset = CourseLesson.objects.all()
    serializer_class = CourseLessonSerializer

class MentorView(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorWorkPlaceView(generics.ListAPIView):
    queryset = MentorWorkPlace.objects.all()
    serializer_class = MentorWorkPlaceSerializer

class MentorAchievementsView(generics.ListAPIView):
    queryset = MentorAchievements.objects.all()
    serializer_class = MentorAchievementsSerializer


class OurProgramView(generics.ListAPIView):
    queryset = OurProgram.objects.all()
    serializer_class = OurProgramSerializer

class FeedbackView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class PartnerView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class FAQView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class WhyUsView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer