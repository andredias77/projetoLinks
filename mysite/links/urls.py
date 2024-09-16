# links/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('criar_pagina_produto/', views.criar_pagina_produto, name='criar_pagina_produto'),
    path('editar_pagina_produto/<int:pagina_id>/', views.editar_pagina_produto, name='editar_pagina_produto'),
    path('pagina_produto/<int:pagina_id>/', views.visualizar_pagina_produto, name='visualizar_pagina_produto'),
    path('minhas_paginas/', views.minhas_paginas, name='minhas_paginas'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('excluir_pagina_produto/<int:pagina_id>/', views.excluir_pagina_produto, name='excluir_pagina_produto'),
    path('excluir_link/<int:link_id>/', views.excluir_link, name='excluir_link'),
    path('gerar_qrcode/<int:pagina_id>/', views.gerar_qrcode, name='gerar_qrcode'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


