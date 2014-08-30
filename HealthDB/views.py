from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def hello(request):
	return render(request, 'index.html')