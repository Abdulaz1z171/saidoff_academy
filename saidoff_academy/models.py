from django.db import models

# Create your models here.

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.title


class ForWhom(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CoursePlan(models.Model):
    total_duration = models.CharField(max_length=100)
    time_for_theory = models.CharField(max_length=100)
    time_for_practice = models.CharField(max_length=100)
    for_theory = models.TextField()
    for_practice = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.title} Plan"


class ComputerFeatures(models.Model):
    processor = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    video_card = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Computer Features for {self.course.title}"


class UserContactAplication(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_checked = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.full_name} for {self.course.title}"


class CourseModule(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.course.title}"


class CourseLesson(models.Model):
    title = models.CharField(max_length=255)
    course_module = models.ForeignKey(CourseModule, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lesson: {self.title} in Module: {self.course_module.title}"


class Mentor(models.Model):
    full_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mentor_images/')
    experience = models.CharField(max_length=255)
    

    def __str__(self):
        return self.full_name


class MentorWorkPlace(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='workplace_logos/')

    def __str__(self):
        return f"Workplace for {self.mentor.full_name}"


class MentorAchievements(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"Achievement: {self.title} by {self.mentor.full_name}"


class OurProgram(models.Model):
    log = models.ImageField(upload_to='our_program_logs/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class OurProgramInfo(models.Model):
    description = models.TextField()
    our_program = models.ForeignKey(OurProgram,on_delete=models.CASCADE)

    def __str__(self):
        return self.our_program.title




class Feedback(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='feedback_images/')
    comment = models.TextField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return f"Feedback by {self.full_name}"


class Partner(models.Model):
    image = models.ImageField(upload_to='partner_images/')

    def __str__(self):
        return "Partner"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class WhyUs(models.Model):
    image = models.ImageField(upload_to = 'why_us_images/')
    title = models.CharField(max_length=250)
    description = models.TextField()


    def __str__(self):
        return self.title

