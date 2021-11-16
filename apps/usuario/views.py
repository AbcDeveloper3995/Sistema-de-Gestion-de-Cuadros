from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import SGPC.settings as setting

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from apps.cuadro.models import Cuadro


class Login(LoginView):
    template_name = 'usuario/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tituloPestaña'] = 'SGPC | Inicio sesion'
        return context


class homeView(LoginRequiredMixin, TemplateView):
    template_name = 'comun/home.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'getGraficoColumn':
                data = {
                    'name':'Porcentaje de ventas',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data':self.getGraficoColumn()
                }
            elif action == 'getGraficoPie':
                data = {
                    'name': 'Porcentaje',
                    'colorByPoint': True,
                    'data': self.getGraficoPie()
                }
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def getGraficoColumn(self):
        data = []
        try:
            for i in range(1, 13):
                total = i+1
                data.append(int(total))
        except:
            pass
        return data

    def getGraficoPie(self):
        data = []
        try:
            for i in Cuadro.objects.all():
                if i.anos_experiencia_rama>0:
                    data.append({'name':i.nombre,
                                 'y':float(i.anos_experiencia_rama)
                                 })
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tituloPestaña'] = 'SGPC | Inicio'
        return context