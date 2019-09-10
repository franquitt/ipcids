from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index_view(request):
    context = {"computadoras":Computadora.objects.all()}
    return render(request, "cidsip/index.html", context)

@csrf_exempt
def actualizar(request, mac, ip):
	if ip=="" or mac =="":
		return JsonResponse({"error": "Faltan datos"})

	try:
		compu = Computadora.objects.get(mac=mac)
	except Computadora.DoesNotExist:
		return JsonResponse({"error": "No existe la computadora"})

	compu.ip="172.16.171."+ip
	compu.save()

	return JsonResponse({"error": "ok"})
