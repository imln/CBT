from django.db import models

# Create your models here.

# model for adding exam
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


# model for adding exam's branch
class ExamBranch(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


# model for adding branch's subject
class BranchSubject(models.Model):
	name = models.CharField(max_length=100)
	ExamBranch = models.ManyToManyField(ExamBranch)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	
# model for adding subject's topic
class SubjectTopic(models.Model):
	name = models.CharField(max_length=100)
	subject_id = models.ForeignKey(BranchSubject, on_delete=models.CASCADE)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name
