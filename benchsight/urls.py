from django.conf.urls import include, url
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='cpu2006', permanent=False), name='index'),
    url(r'cpu2006/', include('cpu2006.urls', namespace='cpu2006', app_name='cpu2006'))
]
