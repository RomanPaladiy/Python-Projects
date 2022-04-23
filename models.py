from django.db import models

# Create your models here.


class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    CourseNum = models.IntegerField( default="")
    Instructor_Name = models.CharField(max_length=30, default="", blank=True, null=False)
    Duration = models.TimeField(max_length="", default="")

    objects = models.Manager()

    def __str__(self):
        return self.Instructor_Name
