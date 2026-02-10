from django.shortcuts import render
from.models import students

# Create your views here.
def getalldata(request):
    data = students.objects.all()
    return render(request,'viewall.html',{'data':data})