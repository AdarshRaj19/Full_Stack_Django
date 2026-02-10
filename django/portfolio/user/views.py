from django.shortcuts import render

# Create your views here.
def home(request):
   # info=['raja','m','Developer',23,'india']
   info= [
  {
    "id": 1,
    "name": "Alice Smith",
    "age": 28,
    "city": "New York"
  },{
    "id": 2,
    "name": "Bob Johnson",
    "age": 35,
    "city": "Los Angeles"
  },
  {
    "id": 3,
    "name": "Charlie Brown",
    "age": 22,
    "city": "Chicago"
  },
  {
    "id": 4,
    "name": "Diana Miller",
    "age": 41,
    "city": "Houston"
  },{
    "id": 5,
    "name": "Eve Davis",
    "age": 30,
    "city": "Miami"}]
   return render(request, 'home.html',{'info':info})

def profile(request):
    return render(request, 'profile.html')

def skills(request):
    return render(request, 'skills.html')

def project(request):
    return render(request, 'project.html')

