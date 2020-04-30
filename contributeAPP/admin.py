from django.contrib import admin

# Register your models here.
from contributeAPP.models import Exam



# Exam models register
class ExamAdmin(admin.ModelAdmin):
	list_display = ['id','name','description']
	ordering = ['id']

admin.site.register(Exam,ExamAdmin)


