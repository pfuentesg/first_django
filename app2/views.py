from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def holi(request):
    return HttpResponse("<em>holi app 2 </em>")