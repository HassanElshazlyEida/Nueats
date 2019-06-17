from django.shortcuts import render
from django.http import HttpResponse
def market(request):
    return render(request,"index.html",)
