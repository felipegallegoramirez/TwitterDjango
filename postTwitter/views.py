from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import user
from django.shortcuts import get_object_or_404

# Create your views here.
def prueba(request):
    return render(request, 'index.html')

def users(request):
    user= list(user.objects.values())
    return JsonResponse(user,safe=False)

def user(request,id):
    user= get_object_or_404(user, id=id)
    return JsonResponse(user.name,safe=False)