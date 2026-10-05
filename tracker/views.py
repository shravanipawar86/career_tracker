from django.shortcuts import render
from.models import Course

def home(request):
    return render(request,'home.html')
def skills(request):
    return render(request,'skills.html')
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})