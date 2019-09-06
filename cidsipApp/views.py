from django.shortcuts import render
from .models import *
# Create your views here.
def index_view(request):
    context = {"computadoras":Computadora.objects.all()}
    return render(request, "cidsip/index.html", context)