from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def homePageView(request):
    return HttpResponse('zaza est ce que tu vois ça ?')
