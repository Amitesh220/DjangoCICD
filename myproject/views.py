from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def status_api(request):
    return JsonResponse({'status': 'Running', 'app': 'DjangoCICD'})
