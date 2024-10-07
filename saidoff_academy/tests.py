from django.test import TestCase
from .models import *
from rest_framework.test import APITestCase
from .serializers import *

# Create your tests here.


class CourseTest(APITestCase):
    def setUp(self):
        self.course  = Course.objects.create(
            title= 'test',
            description = 'test',
            image = 'test.png'
        )

        self.for_whom = ForWhom.objects.create(
            title = 'test',
            description = 'test',
            course = self.course
        )

        self.course_plan = CoursePlan.objects.create(
            time_for_practice = 'test',
            total_duration= 'test',
            time_for_theory= 'test',
            for_practice='test',
            for_theory='test',
            course = self.course
            
        )

        self.computer_features = ComputerFeatures.objects.create(
            processor = 'test',
            cpu = 'test',
            video_card = 'test',
            screen = 'test',
            course = self.course
        )

        self.course_module = CourseModule.objects.create(
            title = 'test',
            course = self.course
        )

    def test_course(self):
        serializer = CourseModelSerializer(self.course)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['title'],'test')
        self.assertEqual(serializer_data['description'],'test')
        self.assertEqual(serializer_data['image'],'/media/test.png')

    
    def test_for_whom(self):
        serializer = ForWhomSerializer(self.for_whom)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['title'],'test')
        self.assertEqual(serializer_data['description'],'test')
        self.assertEqual(serializer_data['course'],self.course.id)

    def test_course_plan(self):
        serializer = CoursePlanSerializer(self.course_plan)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['time_for_practice'],'test')
        self.assertEqual(serializer_data['total_duration'],'test')
        self.assertEqual(serializer_data['time_for_theory'],'test')
        self.assertEqual(serializer_data['for_practice'],'test')
        self.assertEqual(serializer_data['for_theory'],'test')
        self.assertEqual(serializer_data['course'],self.course.id)

    def test_computer_features(self):
        serializer = ComputerFeaturesSerializer(self.computer_features)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['processor'],'test')
        self.assertEqual(serializer_data['cpu'],'test')
        self.assertEqual(serializer_data['video_card'],'test')
        self.assertEqual(serializer_data['screen'],'test')
        self.assertEqual(serializer_data['course'],self.course.id)

    def test_course_module(self):
        serializer = CourseModuleSerializer(self.course_module)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['title'],'test')
        self.assertEqual(serializer_data['course'],self.course.id)


