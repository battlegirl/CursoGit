from django.shortcuts import render, HttpResponse

# Create your views here.
#voy a crar tantas vistas como páginas y url tenga mi sitio

def home(request):

    return render(request, "home.html")


def servicios(request):
    return render(request, "servicios.html")


def tienda(request):
    return render(request, "tienda.html")


def blog(request):
    return render(request, "blog.html")


def contacto(request):
    return render(request, "contacto.html")