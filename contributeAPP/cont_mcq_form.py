from django import forms  
from contributeAPP.models import MCQuestion
class MCQuestionForm(forms.ModelForm):  
	class Meta:  
		model = MCQuestion  
		#fields = ['description','ques_upload','option1','option2','option3','option4','correct_option','solution','sol_upload','level_of_ques','about_question','topic_id']
		fields = "__all__"

	#def __init__(self, *args, **kwargs):
		#self.fields['topic_id'].queryset = SubjectTopic.objects.filter(subject_id=1)