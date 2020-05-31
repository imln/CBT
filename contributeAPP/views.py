from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

from contributeAPP.cont_mcq_form import MCQuestionForm
from contributeAPP.models import SubjectTopic

# def index(request):  
# 	# template = loader.get_template('index.html')  
# 	# return HttpResponse(template.render())    , 'topic_id' : request.GET['t']
# 	mcq = MCQuestionForm()
# 	#mcq.fields['topic_id'] = request.GET['t']
# 	mcq.fields["topic_id"].queryset = SubjectTopic.objects.filter(subject_id=request.GET['s'])
# 	return render(request,"index.html",{'form':mcq})

def index(request):  
	if request.method == "POST":  
		mcq = MCQuestionForm(request.POST)  
		if mcq.is_valid():  
			try:  
				mcq.save()  
				  
			except:  
				pass  
	else:  
		mcq = MCQuestionForm()
		mcq.fields["topic_id"].queryset = SubjectTopic.objects.filter(subject_id=request.GET['s'])
  
	return render(request,'index.html',{'form':mcq}) 

def show(request):
	htm = "<html><body><h3>Thanks.</h3></body></html>"  	
	return HttpResponse(htm) 