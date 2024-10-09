from django.urls import path
from saidoff_academy import views


urlpatterns = [
    path('courses/',views.CourseView.as_view()),
    path('course/<int:pk>/',views.CourseDetailView.as_view()),
    path('for-whoms/',views.ForWhomView.as_view()),
    path('course-plans/',views.CoursePlanView.as_view()),
    path('computer-features/',views.ComputerFeauturesView.as_view()),
    path('user-contact-aplications/',views.UserContactAplicationView.as_view()),
    path('course-modules/',views.CourseModuleView.as_view()),
    path('course-lessons/',views.CourseLessonView.as_view()),
    path('mentors/',views.MentorView.as_view()),
    path('mentor-work-places/',views.MentorWorkPlaceView.as_view()),
    path('our-programs/',views.OurProgramView.as_view()),
    path('feedbacks/',views.FeedbackView.as_view()),
    path('partners/',views.PartnerView.as_view()),
    path('faqs/',views.FAQView.as_view()),
    path('why-us/',views.WhyUsView.as_view())
    
]