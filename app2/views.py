from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def holi(request):
    holi= "bindeando variables"
    return render(request, "index.html", context={"my_var":holi})