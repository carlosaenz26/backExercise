from django.conf.urls import url 
from .views import operaciones,suma,resta

urlpatterns = [ 
    url(r'^api/operaciones$', operaciones),
    url(r'^api/operaciones/suma', suma),
    url(r'^api/operaciones/resta', resta),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]