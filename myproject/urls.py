from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from DjangoCICD minimal project!")

urlpatterns = [
    path('', home),
]
