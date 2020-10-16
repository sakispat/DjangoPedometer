from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Sum
from .models import Step
from .forms import StepForms
import datetime


def index(request):
	return render(request, 'steps/index.html')

def chart(request, dfrom='2020-10-10', dto='2020-10-15'):	
	labels = []
	data = []

	# datefrom = request.GET['datefrom']
	# dateto = request.GET['dateto']

	datefrom = dfrom
	dateto = dto

	# steps = Step.objects.all().values('steps', 'days').order_by('days')
	steps = Step.objects.values('steps', 'days').filter(days__range=(datefrom, dateto)).order_by('days')
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

def ajax_chart(request):
	if request.is_ajax():
		labels = []
		data = []
		datefrom = request.POST.get('datefrom', None) # getting data from input datefrom
		dateto = request.POST.get('dateto', None)  # getting data from input dateto


		if datefrom and dateto: # cheking if datefrom and dateto have value 
			steps = Step.objects.values('steps', 'days').filter(days__range=(datefrom, dateto)).order_by('days')
			for entry in steps:
				labels.append(entry['steps'])
				data.append(entry['days'])
			return JsonResponse(data={'steps': labels, 'days': data})
