from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages import get_messages
from django.utils.http import urlsafe_base64_decode
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import ProcessFormView


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login'
    permission_denied_message = 'Acesso Negado'


class CustomContextMixin(CustomLoginRequiredMixin, ContextMixin):
    """
    Implements method to get default context.
    """

    def get_context_data(self, **kwargs):
        """
        This method initiates the context default.
        """

        context = super(CustomContextMixin, self).get_context_data(**kwargs)

        for msg in get_messages(self.request):
            if msg.level == messages.ERROR:
                context['message'] = msg.message
            elif msg.level == messages.SUCCESS:
                context['message'] = msg.message
        return context


class UpdateMixin(ProcessFormView):
    """
    Implements method to handle post request in update.
    """

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        if 'pk' in kwargs:
            self.pk = kwargs['pk']
        if 'uidb64' in kwargs:
            self.email = urlsafe_base64_decode(kwargs['uidb64'])
        return super(UpdateMixin, self).post(request, *args, **kwargs)

    def __init__(self):
        self.pk = None
        self.email = None


class CustomTemplateView(TemplateView, CustomContextMixin):
    """
    Implements method to get default template.
    """

    def get(self, request, *args, **kwargs):
        return super(CustomTemplateView, self).get(request, *args, **kwargs)


class CustomFormView(FormView):
    """
    Implements method to get default form.
    """

    def get(self, request, *args, **kwargs):
        return super(CustomFormView, self).get(request, *args, **kwargs)
