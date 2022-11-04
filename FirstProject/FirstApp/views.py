from django.shortcuts import render

# Create your views here.
def wishes(request):
    return render(request,'FirstApp/wishes.html')

def hello(request):
    return render(request,'FirstApp/hello.html');
def students(request):
    return render(request,'FirstAPP/students.html');
def students1(request):
    return render(request,'FirstApp/students2.html');
