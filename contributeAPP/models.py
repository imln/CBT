from django.db import models

# Create your models here.

# model for adding exam
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


# model for adding exam
