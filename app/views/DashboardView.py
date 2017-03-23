# Create your views here.
from django.views.generic import TemplateView

from app.mixins import CustomTemplateView


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
