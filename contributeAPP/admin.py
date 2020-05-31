from django.contrib import admin

# Register your models here.
from contributeAPP.models import Exam
from contributeAPP.models import ExamBranch
from contributeAPP.models import BranchSubject
from contributeAPP.models import SubjectTopic
from contributeAPP.models import MCQuestion
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


# MCQuestion  models register
class MCQuestionAdmin(admin.ModelAdmin):
	list_display = ['id','description','ques_upload','option1','option2','option3','option4','correct_option','solution','sol_upload','level_of_ques','about_question','topic_id']
	ordering = ['id']

admin.site.register(MCQuestion,MCQuestionAdmin)