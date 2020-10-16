from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Sum
from .models import Step
from .forms import StepForms


def index(request):
	return render(request, 'steps/index.html')

def home(request):
    return render(request, 'home.html')

def chart(request):	
	labels = []
	data = []
	steps = Step.objects.all().values('steps', 'days').order_by('days')
	for entry in steps:
		labels.append(entry['steps'])
		data.append(entry['days'])
	return JsonResponse(data={'steps': labels, 'days': data})

def create(request):
	if request.method == 'POST':
		form = StepForms(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = StepForms()
	return render(request, 'steps/create.html', {'form': form})
