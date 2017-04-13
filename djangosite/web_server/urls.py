from django.conf.urls import  include, url
from . import views

urlpatterns = (
    url(r'^index$',views.index,name='index'),
    url(r'^web_data_clear$',views.web_data_clear,name='web_data_clear'),
    url(r'^list_mtcd$',views.list_mtcd,name = 'list_mtcd'),
    url(r'^list_mtid$',views.list_mtid,name = 'list_mtid'),
    url(r'^list_index_dict$',views.list_index_dict,name = 'list_index_dict'),
    url(r'^update_dict$',views.update_dict,name = 'update_dict'),
    url(r'^increase_dict$',views.increase_dict,name = 'increase_dict'),
)