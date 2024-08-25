from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people = [
        {'Name': 'Gopi', 'Age': 22},
        {'Name': 'Tanmay', 'Age': 23},
        {'Name': 'Vasu', 'Age': 23},
        {'Name': 'Sagar', 'Age': 22}
    ]
    return render(request, "index.html", context={'peoples':people})
