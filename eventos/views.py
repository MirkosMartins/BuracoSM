from django.shortcuts import render, redirect
from models import *
import floppyforms as forms
from django.contrib.auth.decorators import login_required

class PointWidget(forms.gis.BaseGMapWidget, forms.gis.PointWidget):
   template_name = 'google.html'
   default_lon = '-53.806944'
   default_lat = '-29.684167'

   def get_context_data(self):
       ctx = super(PointWidget, self).get_context_data()
       ctx.update({
           'lon': self.default_lon,
           'lat': self.default_lat,
       })
       return ctx


class EventoForm(forms.ModelForm):
  posicao = forms.gis.PointField(widget=PointWidget(attrs={'map_width': 700, 'map_height': 500, 'require': False}))
  class Meta:
    model = Evento
    exclude = ['usuario']

@login_required
def ve(request):
  form = EventoForm(request.POST or None, request.FILES or None)
  novo = 1

  if form.is_valid():
    buraco = form.save(commit=False)
    buraco.usuario = request.user
    buraco.save()

    return redirect("home")

  return render(request, 've.html', locals())

def home(request, evento=None):
  if evento:
    try:
      evento = Evento.objects.get(id=int(evento))
    except:
      evento = None
        
  eventos = Evento.objects.all()
  home = 1
  #print eventos[0].posicao.tuple[:]

  return render(request, "mapa.html", locals())

@login_required
def meus_buracos(request):
  eventos = Evento.objects.filter(usuario=request.user)
  meus = 1
  return render(request, "mapa.html", locals())
