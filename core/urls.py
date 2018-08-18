from django.urls import path, re_path
from .views import (
    home,

    lista_pessoas, 
    pesoas_novo,
    pessoa_update,
    pessoa_delete,
    
    lista_veiculos, 
    veiculo_novo,
    veiculo_update,
    veiculo_delete,
    
    lista_mov_rotativo,
    mov_rotativo_novo,
    movrotativo_update,
    movrotativo_delete,
    
    lista_mensalistas,
    mensalista_novo,
    mensalista_update,
    mensalista_delete,
    
    lista_movmensalistas,
    movmensalista_novo,
    movmensalista_update,
    movmensalista_delete,
)


urlpatterns = [
    path('', home, name='core_home'),
    
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', pesoas_novo, name='core_pesoas_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoa-delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),
    
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculo-delete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),
    
    path('movsrotativos/', lista_mov_rotativo, name='core_lista_mov_rotativo'),
    path('movsrotativos-novo/', mov_rotativo_novo, name='core_mov_rotativo_novo'),
    re_path(r'^movrotativos-update/(?P<id>\d+)/$', movrotativo_update, name='core_movrotativo_update'),
    re_path(r'^movrotativos-delete/(?P<id>\d+)/$', movrotativo_delete, name='core_movrotativos_delete'),
    
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    re_path(r'^mensalista-delete/(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),
    
    path('movmensalistas/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('movmensalista-novo/', movmensalista_novo, name='core_mov_mensalista_novo'),
    re_path(r'^movmensalista-update/(?P<id>\d+)/$', movmensalista_update, name='core_movmensalista_update'),
    re_path(r'^movmensalista-delete/(?P<id>\d+)/$', movmensalista_delete, name='core_movmensalista_delete'),
]
