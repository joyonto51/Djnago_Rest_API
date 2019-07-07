from django.db import models

# Create your models here.
class Attendance(models.Model):
    school_class = models.CharField(max_length=10)
    section = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=35)
    roll = models.SmallIntegerField()
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.school_class)