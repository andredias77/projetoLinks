from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PaginaProdutoForm, LinkForm
from .models import PaginaProduto, Link
from django.contrib import messages
import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import PaginaProduto
import re


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
    return render(request, 'home.html')

@login_required
def criar_pagina_produto(request):
    if request.method == 'POST':
        form = PaginaProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            pagina = form.save(commit=False)
            pagina.criador = request.user
            pagina.save()
            return redirect('editar_pagina_produto', pagina_id=pagina.id)
    else:
        form = PaginaProdutoForm()
    return render(request, 'criar_pagina_produto.html', {'form': form})


@login_required
def editar_pagina_produto(request, pagina_id):
    pagina = get_object_or_404(PaginaProduto, id=pagina_id, criador=request.user)

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            # Não haverá mais a necessidade de buscar detalhes de produtos pela API
            link.pagina = pagina
            link.save()
            return redirect('editar_pagina_produto', pagina_id=pagina.id)
    else:
        form = LinkForm()

    links = pagina.links.all()
    return render(request, 'editar_pagina_produto.html', {'form': form, 'links': links, 'pagina': pagina})


# links/views.py

def visualizar_pagina_produto(request, pagina_id):
    pagina = get_object_or_404(PaginaProduto, id=pagina_id)
    links = pagina.links.all()
    return render(request, 'visualizar_pagina_produto.html', {'pagina': pagina, 'links': links})

@login_required
def minhas_paginas(request):
    paginas = PaginaProduto.objects.filter(criador=request.user)
    return render(request, 'minhas_paginas.html', {'paginas': paginas})

@login_required
def excluir_pagina_produto(request, pagina_id):
    pagina = get_object_or_404(PaginaProduto, id=pagina_id, criador=request.user)

    if request.method == 'POST':
        pagina.delete()
        return redirect('minhas_paginas')

    return render(request, 'confirmar_exclusao_pagina.html', {'pagina': pagina})

@login_required
def excluir_link(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    pagina = link.pagina
    if pagina.criador != request.user:
        messages.error(request, 'Você não tem permissão para excluir este link.')
        return redirect('editar_pagina_produto', pagina_id=pagina.id)
    if request.method == 'POST':
        link.delete()
        messages.success(request, 'Link excluído com sucesso.')
        return redirect('editar_pagina_produto', pagina_id=pagina.id)
    return render(request, 'confirmar_exclusao_link.html', {'link': link})


@login_required
def gerar_qrcode(request, pagina_id):
    # Obter a página do produto
    pagina = get_object_or_404(PaginaProduto, id=pagina_id, criador=request.user)

    # URL para onde o QR Code irá direcionar
    url_pagina = request.build_absolute_uri(f'/pagina_produto/{pagina_id}/')

    # Gerar o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_pagina)
    qr.make(fit=True)

    # Criar a imagem do QR Code
    img = qr.make_image(fill='black', back_color='white')

    # Retornar a imagem como resposta HTTP com cabeçalho para download
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    
    # Cabeçalho para forçar o download
    response['Content-Disposition'] = f'attachment; filename="qrcode_pagina_{pagina_id}.png"'
    
    return response

def extrair_asin(url):
    # Exemplo de URL: https://www.amazon.com.br/dp/B08XJG8MQM/
    match = re.search(r'/dp/([A-Z0-9]{10})', url)
    if match:
        return match.group(1)
    else:
        return None