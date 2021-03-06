from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, CreateView

from langerak_gkv.activities.models import Activity

from .forms import PrayerOnDemandForm
from .models import PrayerOnDemand


class HomepageView(TemplateView):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        # form initialization is specific to this view, the create view has its
        # own form builder
        kwargs['form'] = PrayerOnDemandForm(request=self.request)
        kwargs['activities'] = list(Activity.objects.homepage().order_by('?')[:4])
        return super(HomepageView, self).get_context_data(**kwargs)


class PODCreateView(CreateView):
    template_name = 'homepage/home.html'
    model = PrayerOnDemand
    form_class = PrayerOnDemandForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super(PODCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        response = super(PODCreateView, self).form_valid(form)
        messages.success(self.request, _('Your request was received, we will pray for you.'))
        # TODO: send e-mail
        return response

    def get_context_data(self, **kwargs):
        context = super(PODCreateView, self).get_context_data(**kwargs)
        context['pod_form'] = context['form']
        return context
