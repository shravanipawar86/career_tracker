from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def skills(request):
    return render(request,'skills.html')