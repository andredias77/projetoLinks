from django.shortcuts import render

# Create your views here.
#Logica por tras do site    

# links/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PaginaProdutoForm, LinkForm
from .models import PaginaProduto, Link


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Substitua 'home' pela sua view inicial
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    pagina = None
    if request.user.is_authenticated:
        try:
            pagina = PaginaProduto.objects.get(criador=request.user)
        except PaginaProduto.DoesNotExist:
            pagina = None
    return render(request, 'home.html', {'pagina': pagina})

@login_required
def criar_pagina_produto(request):
    try:
        pagina = PaginaProduto.objects.get(criador=request.user)
        return redirect('editar_pagina_produto')
    except PaginaProduto.DoesNotExist:
        if request.method == 'POST':
            form = PaginaProdutoForm(request.POST)
            if form.is_valid():
                pagina = form.save(commit=False)
                pagina.criador = request.user
                pagina.save()
                return redirect('editar_pagina_produto')
        else:
            form = PaginaProdutoForm()
        return render(request, 'criar_pagina_produto.html', {'form': form})
    
@login_required
def editar_pagina_produto(request):
    pagina = get_object_or_404(PaginaProduto, criador=request.user)

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.pagina = pagina
            link.save()
            return redirect('editar_pagina_produto')
    else:
        form = LinkForm()

    links = pagina.links.all()
    return render(request, 'editar_pagina_produto.html', {'pagina': pagina, 'form': form, 'links': links})

# links/views.py

def visualizar_pagina_produto(request, pagina_id):
    pagina = get_object_or_404(PaginaProduto, id=pagina_id)
    links = pagina.links.all()
    return render(request, 'visualizar_pagina_produto.html', {'pagina': pagina, 'links': links})
