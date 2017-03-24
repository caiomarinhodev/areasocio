# Create your views here.
# -*- coding: utf-8 -*-
from app.mixins import CustomTemplateView


class DashboardView(CustomTemplateView):
    template_name = 'dashboard.html'
