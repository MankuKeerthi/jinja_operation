from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':7,'b':9,'c':10}
    return render(request,'condition.html',d)
