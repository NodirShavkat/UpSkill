from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='instructors/', blank=True, null=True)
    expertise = models.CharField(max_length=255, help_text="Masalan: Python, Frontend, Data Science")
    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    overview = models.TextField(null=True, blank=True)
    
class Content(models.Model):
    pass
