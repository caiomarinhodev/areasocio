# Create your views here.
from app.mixins import CustomTemplateView


class DashboardView(CustomTemplateView):
    template_name = 'dashboard.html'
