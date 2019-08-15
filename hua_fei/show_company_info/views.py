from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

# def to_index(request):
#     response = HttpResponse(status=302)
#     response['Location'] = '/index.html/'
#     return response

def index(request):

    return render(request, 'index.html')