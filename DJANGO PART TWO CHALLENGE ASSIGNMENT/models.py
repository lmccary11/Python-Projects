from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(default="", max_length=40)
    course_Number = models.IntegerField(default=0, blank=False, null=False)
    instructor_Name = models.CharField(default="", max_length=40, blank=False, null=False)
    duration = models.DecimalField(default=0.00, max_digits=6000, decimal_places=2)
    objects = models.Manager()

