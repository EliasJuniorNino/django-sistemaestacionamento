from django.shortcuts import render, redirect
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    Mensalista,
    MovMensalista,
)
from .forms import (
    PessoaForm, 
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm, 
    MovMensalistaForm,
)

def home(request):
    context = {'mensagem' : 'Ola mundo'}
    return render(request,'core/index.html', context)

''' PESSOAS '''

def lista_pessoas(request):
    context = Pessoa.objects.all()
    formPessoas = PessoaForm()
    data = { 'pessoas' : context, 'form' : formPessoas}
    return render(request, 'core/lista_pessoas.html', data)

def pesoas_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoas_update.html', data)

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_delete_confirm.html', {'pessoa':pessoa})

''' VEICULOS '''

def lista_veiculos(request):
    context = Veiculo.objects.all()
    formVeiculo = VeiculoForm()
    data = { 'veiculos' : context, 'form' : formVeiculo}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_update.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_delete_confirm.html', {'veiculo':veiculo})

''' MOV ROTATIVO '''

def lista_mov_rotativo(request):
    context = MovRotativo.objects.all()
    formMovRotativoForm = MovRotativoForm()
    data = { 'MovRotativos' : context , 'form' : formMovRotativoForm}
    return render(request, 'core/lista_mov_rotativo.html', data)

def mov_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rotativo')

def movrotativo_update(request, id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rotativo')
    else:
        return render(request, 'core/movrotativo_update.html', data)

def movrotativo_delete(request, id):
    movrotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movrotativo.delete()
        return redirect('core_lista_mov_rotativo')
    else:
        return render(request, 'core/movrotativo_delete_confirm.html', {'movrotativo':movrotativo})

''' MENSALISTAS '''

def lista_mensalistas(request):
    context = Mensalista.objects.all()
    form = MensalistaForm()
    data = { 'mensalistas' : context, 'form' : form}
    return render(request, 'core/lista_mensalistas.html', data)
    
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')

def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/mensalista_update.html', data)

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/mensalista_delete_confirm.html', {'mensalista':mensalista})

''' MOV MENSALISTAS '''

def lista_movmensalistas(request):
    context = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = { 'movmensalistas' : context, 'form' : form }
    return render(request, 'core/lista_movmensalistas.html', data)

def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')

def movmensalista_update(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/movmensalista_update.html', data)

def movmensalista_delete(request, id):
    movmensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/movmensalista_delete_confirm.html', {'movmensalista':movmensalista})