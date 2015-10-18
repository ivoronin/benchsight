from django import forms
from .models import Result

HW_VENDORS = Result.objects.values_list("hardware_vendor", "hardware_vendor").distinct()
BENCHMARKS = Result.objects.values_list("benchmark", "benchmark").distinct()

class FilterForm(forms.Form):
    benchmark = forms.ChoiceField(label="Benchmark", initial="CINT2006rate", choices=BENCHMARKS)
    min_year = forms.DateField(label="Minimum year", input_formats=['%Y'], required=False)
    max_year = forms.DateField(label="Maximum year", input_formats=['%Y'], required=False)
    min_chips = forms.IntegerField(label="Minimum chips", min_value=1, required=False)
    max_chips = forms.IntegerField(label="Maximum chips", min_value=2, required=False)
    vendor = forms.ChoiceField(label="Vendor", required=False, choices=[('', '')] + list(HW_VENDORS))
    system = forms.CharField(label="System name", required=False)
    processor = forms.CharField(label="CPU Model", required=False)
