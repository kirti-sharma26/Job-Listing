from django.shortcuts import render
from .models import *
from job.settings import BASE_DIR

# Create your views here.
def index(request):
    job = Job.objects.all()
    return render(request, 'index.html', {'Job':job, 'BASE_DIR':BASE_DIR})

def admin1(request):
    if request.method == 'POST':
        job = Job()
        job.title = request.POST.get("title", False)
        job.company_name = request.POST.get("comapny_name", False)
        job.description = request.POST.get("description", False)
        job.location = request.POST.get("location", False)
        job.requirements = request.POST.get("requirements", False)
        job.app_deadline = request.POST.get("app_deadline", False)
        job.save()
        return render(request, 'requested.html')    
    return render(request, 'admin.html')

def apply(request):
    if request.method == 'POST':
        apply = Apply()
        apply.name = request.POST.get("name", False)
        apply.dob = request.POST.get("dob", False)
        apply.ten_marks = request.POST.get("ten_marks", False)
        apply.twelve_marks = request.POST.get("twelve_marks", False)
        apply.yoe = request.POST.get("yoe", False)
        apply.save()
        return render(request, 'applied.html')    
    return render(request, 'apply.html')