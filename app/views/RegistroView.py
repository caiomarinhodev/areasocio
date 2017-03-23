# Create your views here.

from app.mixins import CustomFormView


class RegistroView(CustomFormView):
    template_name = 'registro.html'
    success_url = '/login'
