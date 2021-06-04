from django.shortcuts import render, get_object_or_404
from .models import job

def home(request):
    jobs = job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, jobs_id):
    detailjob = get_object_or_404(job, pk=jobs_id)    
    return render(request, 'jobs/detail.html', {'job':detailjob})