from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.ResultDetailView.as_view(), name='result_detail'),
    url(r'^$', views.ResultsListView.as_view(), name='results_list'),

]
