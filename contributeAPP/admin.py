from django.contrib import admin

# Register your models here.
from contributeAPP.models import Exam
from contributeAPP.models import ExamBranch
from contributeAPP.models import BranchSubject
from contributeAPP.models import SubjectTopic

# Exam models register
class ExamAdmin(admin.ModelAdmin):
	list_display = ['id','name','description']
	ordering = ['id']

admin.site.register(Exam,ExamAdmin)


# ExamBranch models register
class ExamBranchAdmin(admin.ModelAdmin):
	list_display = ['id','name','description','exam_id']
	ordering = ['id']

admin.site.register(ExamBranch,ExamBranchAdmin)


# BranchSubject models register
class BranchSubjectAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	ordering = ['id']

admin.site.register(BranchSubject,BranchSubjectAdmin)


# SubjectTopic models register
class SubjectTopicAdmin(admin.ModelAdmin):
	list_display = ['id','name','subject_id']
	ordering = ['id']

admin.site.register(SubjectTopic,SubjectTopicAdmin)