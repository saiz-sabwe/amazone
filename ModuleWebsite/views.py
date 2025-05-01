from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": 'titre de la vue'
    }
    return render(request, "ModuleWebsite/index_.html", context)

def about(request):
    context = {
        "title": 'titre de la vue'
    }
    return render(request, "ModuleWebsite/about-us.html", context)

def location(request):
    context = {
        "title": 'titre de la vue'
    }
    return render(request, "ModuleWebsite/about-us-locations.html", context)

def safety(request):
    context = {
        "title": 'titre de la vue'
    }
    return render(request, "ModuleWebsite/safety.html", context)

def drilling(request):
    context = {
        "title": 'titre de la vue'
    }
    return render(request, "ModuleWebsite/drilling.html", context)