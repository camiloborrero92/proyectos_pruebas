from django.shortcuts import render
from principal.models import Persona

# Create your views here.
def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request,'index.html',contexto)