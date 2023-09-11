from django.shortcuts import render, redirect
from AppLigaDeFutbol.forms import JugadorFormulario, DirectorTecnicoFormulario, ClubFormulario, OfertaFormulario, JugadorBusquedaFormulario, UserEditForm
from .models import Jugador, Oferta
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "inicio.html")

# def agregar_jugador(request):
#     if request.method == 'POST':
#         form = JugadorFormulario(request.POST)
#         form.instance.usuario = request.user
#         # usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
#         # usuario.avatar.save()
#         form.instance.imagen = request.POST.get('imagen')
#         if form.is_valid():
#             form.save()
#             jugador = form.save()
#             jugador.imagenjugador.imagen = request.POST.get('imagen')
#             jugador.imagenjugador.save()
#             return redirect('Inicio')
#     else:
#         form = JugadorFormulario()
#     return render(request, 'jugador_formulario.html', {'form': form})

class crear_jugador(CreateView):
    model = Jugador
    form_class = JugadorFormulario
    success_url = reverse_lazy('Inicio')
    template_name = 'jugador_formulario.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(crear_jugador, self).form_valid(form)

class editar_jugador(UpdateView):
    model = Jugador
    template_name = 'jugador_formulario.html'
    fields = ['nombre', 'apellido', 'posicion', 'promedio', 'pierna_habil', 'transferible', 'imagen']
    success_url = reverse_lazy('JugadoresPlantilla')

def ver_jugador(request, id, plantilla):
    jugador = Jugador.objects.get(pk=id)
    ofertas = Oferta.objects.filter(jugador__nombre=jugador.nombre)
    return render(request, 'jugador_ver.html', {'jugador': jugador, 'plantilla': plantilla, 'ofertas': ofertas})

def ofertar_jugador(request, id, ver_jugador):
    if request.method == 'POST':
        form = OfertaFormulario(request.POST)
        jugador = Jugador.objects.get(pk=request.POST.get("jugador_id"))
        usuario_nombre = request.POST.get("usuario_nombre")
        form.instance.jugador = jugador
        form.instance.usuario_nombre = usuario_nombre
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        jugador = Jugador.objects.get(pk=id)
        form = OfertaFormulario()
        form.instance.jugador = jugador
    return render(request, 'jugador_ofertar.html', {'form': form, 'jugador': jugador, 'ver_jugador': ver_jugador})

class listar_jugadores_transferibles(ListView):
    template_name = 'jugadores_transferibles.html'
    context_object_name = 'jugadores'
    model = Jugador
    
class listar_jugadores_plantilla(ListView):
    template_name = 'jugadores_plantilla.html'
    context_object_name = 'jugadores'
    model = Jugador
    
class eliminar_jugador(DeleteView):
    model = Jugador
    template_name = 'jugador_eliminar.html'
    success_url = reverse_lazy('JugadoresPlantilla')
    
def agregar_director_tecnico(request):
    if request.method == 'POST':
        form = DirectorTecnicoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = DirectorTecnicoFormulario()
    return render(request, 'director_tecnico_formulario.html', {'form': form})


def agregar_club(request):
    if request.method == 'POST':
        form = ClubFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BuscarJugadoresPorNombre')
    else:
        form = ClubFormulario()
    return render(request, 'club_formulario.html', {'form': form})


def buscar_jugadores_por_nombre(request):
    jugadores = []
    form = JugadorBusquedaFormulario(request.GET)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Realizar la búsqueda en el modelo Jugador por nombre
        if nombre:
            jugadores = Jugador.objects.filter(nombre__icontains=nombre)

    return render(request, 'jugadores_buscar.html', {'form': form, 'jugadores': jugadores})


def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
                
            miFormulario.save()
            return redirect('Inicio')
    else:
        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
        return render(request, 'perfil_editar.html', {'miFormulario': miFormulario, 'usuario': usuario.username})

# class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
#     template_name = 'cambiar_contrasenia.html'
#     success_url = reverse_lazy('EditarPerfil')
    