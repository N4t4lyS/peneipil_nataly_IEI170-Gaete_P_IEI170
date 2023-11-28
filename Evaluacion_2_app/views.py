from django.shortcuts import render,redirect

# Create your views here.
from Evaluacion_2_app.models import Reserva
from Evaluacion_2_app.forms import formReserva

def index(request):
    return render(request,'index.html')

def crear_reserva(request):
    form = formReserva()
    if request.method=='POST':
        form = formReserva(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('listado_reservas')
    data = {'form': form}
    return render(request, 'crearReserva.html', data)

def listado_reservas(request):
    reservas = Reserva.objects.all()
    data ={'reservas': reservas}
    return render(request,'reservas.html',data)




def eliminarReservas(request, IN_id):
    reservas = Reserva.objects.get(id = IN_id)
    reservas.delete()
    return redirect('/reservas')

def modificarReservas(request, IN_id):
    reservas = Reserva.objects.get(id = IN_id)
    form = formReserva(instance=reservas)

    if (request.method == 'POST'):
        form = formReserva(request.POST, instance=reservas)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')
  
    data = {'form': form}
    return render (request, 'crearReserva.html', data)