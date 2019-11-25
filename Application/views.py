from django.shortcuts import render
from .models import Game 
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, Http404
# Create your views here.

def home(request):
    return render(request, 'Application/index.html', locals())


def create(request):
    if request.method == "POST":
        nom = request.POST.get('nom').capitalize()
        prenom = request.POST.get('prenom').capitalize()
        mail = request.POST.get('mail').lower()
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        username = f"{nom}.{prenom}"

        if len(User.objects.filter(email=mail) == 1):
            return HttpResponse("Vous avez déjà un compte")

        usr = User(username=username, password=password, email=mail, first_name=nom, last_name=prenom)

        usr.save()

        return HttpResponse(1)

    raise Http404("Chemin Non Trouvé")
