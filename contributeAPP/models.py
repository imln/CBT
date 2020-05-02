from django.db import models
from django.contrib import staticfiles
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

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


# model for adding mcq question , one correct answer
CORRECT_OPTION_CHOICES = [
	('A', '1'),
	('B', '2'),
	('C', '3'),
	('D', '4'),
]

LEVEL_OF_QUES = [
	('E', 'Easy'),
	('M', 'Medium'),
	('H', 'Hard'),
]
class MCQuestion(models.Model):
	description = models.TextField()
	ques_upload = models.ImageField(upload_to= "questionIMG/%Y/%m/%d/")
	option1 = models.CharField(max_length=300)
	option2 = models.CharField(max_length=300)
	option3 = models.CharField(max_length=300)
	option4 = models.CharField(max_length=300)	
	correct_option = models.CharField(max_length=1, choices=CORRECT_OPTION_CHOICES)
	solution = models.TextField()
	sol_upload = models.ImageField(upload_to= "solutionIMG/%Y/%m/%d/")
	level_of_ques = models.CharField(max_length=1, choices=LEVEL_OF_QUES)
	about_question = models.CharField(max_length=300)
	topic_id = models.ForeignKey(SubjectTopic, on_delete=models.CASCADE)

	class Meta:
		ordering = ['id']

	# def __str__(self):
	# 	return self.description


#image deleteion after admin delete the row in database
@receiver(post_delete, sender=MCQuestion)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)