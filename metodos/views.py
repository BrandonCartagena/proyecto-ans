from django.shortcuts import render
from metodos import unidad2

def index(request):
	return render(request, 'index.html')

def integrantes(request):
	return render(request, 'integrantes.html')

def info(request):
	return render(request, 'info.html')

def biseccion(request):
	if request.method == 'POST':
		try:
			f_x = request.POST['f_x']
			x1 = float(request.POST['x1'])
			x2 = float(request.POST['x2'])
			cifras = int(request.POST['cifras'])
			data = unidad2.biseccion(f_x, x1, x2, cifras if cifras > 0 else 1)
			return render(request, 'unidad2/biseccion.html', {
				'data': data, 
				'form_data': request.POST
			})
		except:
			return render(request, 'unidad2/biseccion.html', {
				'error': 'Debes introducir datos validos', 
				'form_data': request.POST
			})
	return render(request, 'unidad2/biseccion.html')

def falsa_posicion(request):
	return render(request, 'unidad2/falsa_posicion.html')