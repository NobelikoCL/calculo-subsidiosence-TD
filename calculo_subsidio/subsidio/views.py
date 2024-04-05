# subsidio/views.py

from django.shortcuts import render

def calcular_subsidio(request):
    if request.method == 'POST':
        # Extracción de datos del POST request para el cálculo
        modulos_completados = {
            'modulo1': int(request.POST.get('modulo1', 0)),
            'modulo2': int(request.POST.get('modulo2', 0)),
            'modulo3': int(request.POST.get('modulo3', 0)),
            # Asegúrate de continuar para todos los módulos...
        }
        horas_completadas = sum([v for k, v in modulos_completados.items()])
        porcentaje_avance = horas_completadas / 462 * 100
        pago = porcentaje_avance / 100 * 464000
        
        return render(request, 'resultado.html', {
            'porcentaje_avance': porcentaje_avance,
            'pago': pago,
        })

    # Si no es una solicitud POST, simplemente renderiza el formulario
    return render(request, 'index.html')
