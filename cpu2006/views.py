from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from .models import Result
from .forms import FilterForm


class ResultDetailView(DetailView):
    model = Result


class ResultsListView(FormMixin, ListView):
    model = Result
    paginate_by = 18
    form_class = FilterForm
    ordering = '-baseline'

    def get_form(self):
        if 'benchmark' in self.request.GET:
                return self.form_class(data=self.request.GET)
        else:
            return self.form_class()

    def get_context_data(self, **kwargs):
        context = super(ResultsListView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_queryset(self):
        form = self.get_form()
        qs = Result.objects.order_by(self.ordering)
        if form.is_valid():
            benchmark = form.cleaned_data['benchmark']
            min_year = form.cleaned_data['min_year']
            max_year = form.cleaned_data['max_year']
            min_chips = form.cleaned_data['min_chips']
            max_chips = form.cleaned_data['max_chips']
            vendor = form.cleaned_data['vendor']
            system = form.cleaned_data['system']
            processor = form.cleaned_data['processor']
            if benchmark:
                qs = qs.filter(benchmark=benchmark)
            if min_year:
                qs = qs.filter(test_date__gte=min_year)
            if max_year:
                qs = qs.filter(test_date__lte=max_year)
            if min_chips:
                qs = qs.filter(num_chips__gte=min_chips)
            if max_chips:
                qs = qs.filter(num_chips__lte=max_chips)
            if vendor:
                qs = qs.filter(hardware_vendor=vendor)
            if system:
                qs = qs.filter(system__icontains=system)
            if processor:
                qs = qs.filter(processor__icontains=processor)
        return qs
